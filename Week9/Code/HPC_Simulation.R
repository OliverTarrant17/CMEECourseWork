
rm(list=ls())
graphics.off()

######################### Functions from first part ################
species_richness <- function(community) {
  richness <- length(unique(community))
  return(richness)
}


choose_two <- function(x) {
  y <- sample(1:x,2, replace = FALSE)
  return(y)
}

initialise_min <- function(size){
  init_min <- rep(1,size)
  return(init_min)
}

neutral_step_speciation <- function(community,v){
  step <- choose_two(length(community)) # call choose two to get indicies of the species which dies and that whose offspring takes over  
  p <- runif(n=1,min=0,max=1)
  if(p>=1-v){
    new <- c(1:(max(community)+1)) # create a new vector of elements up to the max+1 so there is atleast one new unique value
    new <- min(new[!new %in% community]) # select the minimum value not already used
    community[step[1]] <- new
    return(community)
  }
  else{
    community[step[1]] <- community[step[2]]# set p = 1 with prob 0.2, p = 0 with prob 0.8
    return(community)
  }
}

neutral_generation_speciation <- function(community,v){
  x <- length(community)
  i = 0
  while (i<ceiling(x/2)){ # deal with odd numbers
    i <- i+1
    community <- neutral_step_speciation(community,v)
  }
  return(community)
}

species_abundance <- function(community){
  abundances <- as.numeric(table(community)) # get species abundencies
  sorted <- sort(abundances,decreasing=TRUE) # sort abundancies
  return(sorted)
}

octaves <- function(abundancies){
  octave <- tabulate(floor(log(abundancies,base = 2))+1) # takes the log of the abundancies base 2 to specify what bin to put it in. Use floor to ensure all values
  # are rounded down so that upper bound is strict. add 1 to each value so that the first entry is those which are 
  # would otherwise read 0 (those with abundancy >=2^0 but <2^1)
  return(octave)
}

######################### New code ###############

###### 17. Cluster run
###### parameters:
# size - community size
# speciation rate - see v in previous Natural_theroy.R code with code for speciations
# wall time - length of time to run simulation for (in mins)

cluster_run <- function(speciation_rate, size, wall_time, interval_rich, interval_oct, burn_in_generations, output_file_name){
  t1 <- proc.time()[3]
  community <- initialise_min(size)  # set the initial community
  t0 <- proc.time()[3] # record initial time
  wall_time_secs <- 60*wall_time # convert the entered time to seconds
  count = 1   # 
  richness_time_series <- (species_richness(community))
  octs <- list(octaves(species_abundance(community)))
  while((proc.time()[3]-t0) < wall_time_secs){
      community <- neutral_generation_speciation(community,speciation_rate)
      count <- count+1
      if((count <= burn_in_generations)&(count%%interval_rich==0)){
          richness_time_series <- append(richness_time_series,species_richness(community))
      }
      if(count%%interval_oct==0){
          octs <- c(octs,list(octaves(species_abundance(community))))
    }
  }
  # relevent information to store in the output data file
final_community = community
total_time <- proc.time()[3]-t1
parameters <- data.frame(Speciation_Rate=speciation_rate,Size=size,Wall_Time=wall_time,Interval_Richness=interval_rich,Interval_Octave=interval_oct,Burn_in_Generations=burn_in_generations)
save(parameters,richness_time_series,octs,final_community,total_time,file=paste(output_file_name))
}


#iter <- as.numeric(Sys.getenv("PBS_ARRAY_INDEX")) # creates an iterator that will be assigned on the cluster
iter <- 2  # iter for use locally
set.seed(iter) # set a unique seed for each iter
if(iter%%4==1) { # splits the iterations into 4 classes to assign different population sizes
  J=500
}else if(iter%%4==2){
    J=1000
}else if (iter%%4==3){
      J=2500
}else {J=5000}

filename = paste0("Results",iter,".rda")
# My unique speciation rate = 0.004361
cluster_run(0.004361,J,11.5*60,1,round(J/10),8*J,filename)



