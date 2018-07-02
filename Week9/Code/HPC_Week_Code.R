### HPC week code for submission

rm(list=ls())
graphics.off()



##### 1. Define a function to return the number of different species in an input vector
species_richness <- function(community) {
  richness <- length(unique(community)) # counts a vector of the unique occurances in community
  return(richness)
}

##### 2. Function to generate an initial state for the simulation community with max possible number of 
##### species for the community of size given by the input number variable size
initialise_max <- function(size) {
  init_max <- seq(1 : size) 
  return(init_max)
}

##### 3. Function to generate an alternative initial state for the simulation with minimum number of species
##### i.e monodominance
initialise_min <- function(size){
  init_min <- rep(1,size) # assigns 1 to each individual
  return(init_min)
}

##### 4. A function to choose two unique random numbers from a uniform(1,x) dist
choose_two <- function(x) {
  y <- sample(1:x,2, replace = FALSE) #  chooses 2 numbers between 1 to x without replacement
  return(y)
}

##### 5. Function to perform a single step of neutral model selection without speciation on a community vector

neutral_step <- function(community){
  step <- choose_two(length(community)) # call choose two to get indicies of the species which dies and that whose offspring takes over
  community[step[1]] <- community[step[2]] # replace the entry of the first index of step with the second
  return(community)
}

##### 6. Function to simulate several neutral_steos on a community so that a generation has passed
##### If x individuals in community then x/2 neutral steps correspsonds to a complete generation for the taxa being simulated
##### A generation is the amount of time expected between birth and reproduction

neutral_generation <- function(community){
  x <- length(community)
  i = 0
  while (i<ceiling(x/2)){ # deal with odd numbers
    i <- i+1
    community <- neutral_step(community)
  }
  return(community)
}


##### 7. Function doing a neutral theory simulation and return a time series of species richness in the system
##### Should take two inputs, initial= initial community vector, duration=number of generations it is run for

neutral_time_series <- function(initial,duration){ # inital must be a vector entry
  out <- (species_richness(initial)) # set initial value of vector
  community <- initial 
  for (i in 2:(duration+1)) { # loop through remaining elements for the vector
    community <- neutral_generation(community)
    out[i]<-species_richness(community)
  }
  return(out)
}


##### 8. plot the tie series graph
question_8 <- function(initial=initialise_max(100),duration=200){
  y <- neutral_time_series(initial,duration)
  plot(0:duration,y,type="l", main="Neutral theory time series of 100 species",
       xlab="Generation",ylab="Species", col="red")
}


##### 9. Function to perform a step of neutral model with speciation
##### i.e speciation will replace a dead individual with a new species with prob v
##### else the replaced as before
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


##### 10. Function for neutral simulation with speciation
neutral_generation_speciation <- function(community,v){
  x <- length(community)
  i = 0
  while (i<ceiling(x/2)){ # deal with odd numbers
    i <- i+1
    community <- neutral_step_speciation(community,v)
  }
  return(community)
}

##### 11. Function that produces a neutral simulation with speciation
neutral_time_series_speciation <- function(community,v,duration){
  out <- (species_richness(community)) # set initial value of vector
  for (i in 2:(duration+1)) { # loop through remaining elements for the vector
    community <- neutral_generation_speciation(community,v)
    out[i]<-species_richness(community)
  }
  return(out)
}

##### 12. Plot of species richness simulated with speciation using v=0.1
##### initial community size of 100 and run for 200 generations.
##### plot in blue the simulation for initialise_max and red for 
##### the initialise_min
question_12 <- function(community_size=100,v=0.1,duration=200){
  y_min <- neutral_time_series_speciation(initialise_min(community_size),v,duration)
  y_max <- neutral_time_series_speciation(initialise_max(community_size),v,duration)
  plot(0:duration,y_min,type="l", main="Neutral theory time series of a community over 200 generations with speciation rate 0.1",
       xlab="Generation",ylab="Species", col="red",xlim =c(0,duration),ylim =c(0,community_size))
  lines(0:duration,y_max, type="l", col="blue")
  legend(x=120,y=90,c("Initial species = 100","Initial species = 1"),
         cex=0.5,lty=c(1,1), col=c("blue","red"))
}


##### 13. Abundance of species in the system

species_abundance <- function(community){
  abundances <- as.numeric(table(community)) # get species abundencies
  sorted <- sort(abundances,decreasing=TRUE) # sort abundancies
  return(sorted)
}


##### 14. function to bin abundances of species

octaves <- function(abundancies){
  octave <- tabulate(floor(log(abundancies,base = 2))+1) # takes the log of the abundancies base 2 to specify what bin to put it in. Use floor to ensure all values
  # are rounded down so that upper bound is strict. add 1 to each value so that the first entry is those which are 
  # would otherwise read 0 (those with abundancy >=2^0 but <2^1)
  return(octave)
}

##### 15. function that sums vectors

sum_vec <- function(x,y){
  diff <- length(x)-length(y)
  zeros <- rep(0,abs(diff)) # create a vector of zeros to add to the shorter vector
  if(diff<0){ 
    x<-append(x,zeros)   # append the zeros vector to the shorter vector
  }else{ y<-append(y,zeros)}
  return(x+y)
}

##### 16. neutral model simulation. Initial community size =100, v= 0.1, duration=200,
question_16 <- function(community_size=100,duration=200,v=0.1){
  community <- initialise_max(community_size)
  for (i in 2:(duration+1)) { # loop through remaining elements for the vector
    community <- neutral_generation_speciation(community,v)
  }
  # now have community after burn in period
  res <- octaves(species_abundance(community))
  count <- 1
  for(i in 1:2000){
    community <- neutral_generation_speciation(community,v)
    if(i%%20==0){ # check for the values that are multiples of 20
      res <- sum_vec(res,octaves(species_abundance(community)))
      count <- count+1 # increase the count for each new octave added
    }
    
  }
  res <- res/count # take the average of res
  xx <- barplot(res, main = "Mean species abundancies over 2000 generation after a 200 generation burn in period", xlab="Octave",ylab="Mean abundance",
                ylim=c(0,max(res)+1),col=c("red","magenta","blue","yellow","green","orange"),names.arg = c("1","2","3","4","5","6"), axes=TRUE)
  text(x=xx,y=res,label = res,pos=3,cex=0.4,col="black" )
}

##### Challenege A

challenge_A <- function(community_size=100,v=0.1,duration=200,repeats=100){
  YMin <- list(neutral_time_series_speciation(initialise_min(community_size),v,duration)) # First simulation for 1 species
  YMax <- list(neutral_time_series_speciation(initialise_max(community_size),v,duration)) # First simulation for 100 species
  count <- 1
  for(i in 2:repeats){
    a <-neutral_time_series_speciation(initialise_min(community_size),v,duration) # The other simulations
    b <-neutral_time_series_speciation(initialise_max(community_size),v,duration)
    YMin <- c(YMin,list(a))
    YMax <- c(YMax,list(b))
    count <- count+1
  }
  Mean_min <- (0) # Create empty values for the values wanted to record
  Mean_max <-(0)
  var_min<-(0)
  var_max<-(0)
  SE_min<-(0)
  SE_max<-(0)
  CI_Min_U<-(0)
  CI_Min_L<-(0)
  CI_Max_U<-(0)
  CI_Max_L<-(0)
  for(i in 1:duration){
    Mean_min[i] <- mean(unlist(lapply(YMin,`[[`,i)))  # Create a vector of means
    Mean_max[i] <- mean(unlist(lapply(YMax,`[[`,i))) 
    var_min[i]<-var(unlist(lapply(YMin,`[[`,i))) #creates a vector of variance at each time step 
    var_max[i]<-var(unlist(lapply(YMax,`[[`,i)))
    SE_min[i]<-(var_min[i]^0.5)/repeats # creates a vector or standard error at each time step.
    SE_max[i]<-(var_max[i]^0.5)/repeats^0.5
    CI_Min_U[i] <- Mean_min[i]+SE_min[i]*qnorm(0.986)  # Calculate the 92.7% confidence interval for each time point
    CI_Min_L[i] <- Mean_min[i]-SE_min[i]*qnorm(0.986)
    CI_Max_U[i] <- Mean_max[i]+SE_max[i]*qnorm(0.986)
    CI_Max_L[i] <- Mean_max[i]-SE_max[i]*qnorm(0.986)
  }
  par(mfrow=c(2,1))
  plot(c(1:duration),Mean_min,"l",col="red")
  lines(c(1:duration),CI_Min_U,"l",col="blue")
  lines(c(1:duration),CI_Min_L,"l",col="blue")
  legend(x=120,y=15,c("Average species","97.2% confidence interval"),
         cex=0.5,lty=c(1,1), col=c("red","blue"))
  plot(c(1:duration),Mean_max,"l",col="black")
  lines(c(1:duration),CI_Max_U,"l",col="green")
  lines(c(1:duration),CI_Max_L,"l",col="green")
  legend(x=120,y=90,c("Average species","97.2% confidence interval"),
         cex=0.5,lty=c(1,1), col=c("black","green"))
}

###### Challenge B

#challenge_B <- function(){

#}

###### Challenge D 
### J = commnity size, v = speciation rate
challenge_D <- function(J=100,v=0.1){
  p=1 # set a counter for the place number in abundancies
  lineages <- rep(1,J) # creates the community of individuals each is currently a 1 as don't know if any share their types 
  abundancies <- (0) # create a blank abundancies vecotr
  N=J # Set the size if the number of lineages left
  theta=v*(J-1)/(1-v) # probability of coalescence
  while(N>1){
    x <- runif(1,0,N) 
    j <- ceiling(x) # random index of lineages
    randnum <- runif(1,0,1)  # random number (0,1)
    if(randnum<(theta/(theta+N-1))){ # If coalescence occurs
      abundancies[p] <- lineages[j] # know there are this many of this type in the final community
      p<-p+1 # move abundancies placement
    }else{
      i=ceiling(runif(1,0,N)) # choose another random index
      while(i==j){
        i=ceiling(runif(1,0,N)) # ensure index is different
      }
      lineages[i]<-lineages[i]+lineages[j] # sum the two indices together as these are the same type so there are the sum of the two number of this type.
    }
    lineages<-lineages[-j] # remove the additional lineage from the calculations
    N<-N-1 # counter of number of lineages decreases
  }
  abundancies[p]<-lineages # add final lineage to abundancies
  return(abundancies) # return the results
}


########################## HPC CODE ###############

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
# cluster_run(0.004361,J,11.5*60,1,round(J/10),8*J,filename) ### Calls the function and runs it on HPC


#### Fractals in nature questions

##### 21. Fractal dimensions. Formula is  D= log(N)/log(r) where N is the number of smaller objects in the iteration and r is the size ratio from a zero iteration
##### so for the Sierpinski carpet D=log(8)/log(3) = 1.892789... and for Menger sponge D=log(20)/log(3) = 2.726833...

##### 22. The chaos game

chaos_game <- function(repeats=100){
  a <- c(0,0) ; b <- c(3,4) ; c <- c(4,1) # set the corners for the triangle
  X <- c(0,0) # set an initial start point
  plot(X[1],X[2],type="p", col ="black", cex=0.2, xlim = c(-1,5),ylim = c(-1,5)) #plot the start point small
  randoms <- runif(repeats,min=0,max=3) # generate the a rendom selection from the points the number of times that repeats is
  for(i in 1:repeats){
    if(randoms[i]<=1){
      dir=a
    }else if((randoms[i]>1)&(randoms[i]<=2)){
      dir=b
    }else if(randoms[i]>2){
      dir=c
    }
    X=(X+dir)/2 # move the point half way to the choosen point
    lines(X[1],X[2],type = "p",col="black",cex=0.2) #draw the new point
  }
}

##### Challeneg E, Allows you to specify the 3 corners for the triangle and initial start point

challenge_E <- function(initial_X=c(0,0),repeats=100,coloured=20,a=c(0,0),b=c(3,4),c=c(4,12)){
  X <- initial_X
  plot(X[1],X[2],type="p", col ="red", cex=0.2, xlim = c(-1,5),ylim = c(-1,5)) #plot the start point small
  a=a;b=b;c=c
  randoms <- runif(repeats,min=0,max=3) # generate the a rendom selection from the points the number of times that repeats is
  for(i in 1:repeats){
    if(randoms[i]<=1){
      dir=a
    }else if((randoms[i]>1)&(randoms[i]<=2)){
      dir=b
    }else if(randoms[i]>2){
      dir=c
    }
    X=(X+dir)/2 # move the point half way to the choosen point
    if(i < coloured){
      lines(X[1],X[2],type = "p",col="red",cex=0.2)
    }else{
      lines(X[1],X[2],type = "p",col="black",cex=0.2) #draw the new point
    }
  }
  
}


##### 23. Turtle,  direction taken in degrees clockwise with 0 radians being horizontal right going anticlockwise. Note direction in radians not degrees

turtle <- function(start_position,direction,length){
  endpoint_x <- start_position[1]+length*cos(direction) # calculate the endpoints for the line converting between radians and degrees
  endpoint_y <- start_position[2]+length*sin(direction)
  endpoint <- c(endpoint_x,endpoint_y)
  segments(x0=start_position[1],y0=start_position[2],x1=endpoint_x,y1=endpoint_y,col="dark green")
  return(endpoint)
}

##### 24. Elbow, two iterations of turtle, changing angle by 45 degrees clockwise and making length 0.95 original length for second iteration

elbow <- function(starting_point,initial_direction,len){
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,length = len) 
  turtle(start_position = endpoint,direction=initial_direction-45,length=0.95*len)
}

##### 25. Spiral # creates a spiral by repeating elbow. However, runs with an erroo as creates an infinite loop

spiral <- function(starting_point,initial_direction,len){ 
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,length = len)
  spiral(endpoint,initial_direction-45,0.95*len)
}

##### 26. Spiral 2 # solves the infinite loop in spiral and creates a spiral until the line length is shorter than the specified value min_length

spiral2 <- function(starting_point,initial_direction,len,min_length=0.01){
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  if(length>min_length){
    length = (length*0.95)
    spiral2(endpoint,initial_direction-45,length,min_length)
    
  }
}

###### 27. tree 

tree <- function(starting_point,initial_direction,len,min_length=0.01){
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  if(length>min_length){ # check line length is still big enough
    length = (length*0.65) # shortens line
    tree(endpoint,initial_direction-45,length,min_length)  # plots spirallig to the right
    tree(endpoint,initial_direction+45,length,min_length) # plots spiralling to the left
    
  }
  
}

###### 28. fern 

fern <- function(starting_point,initial_direction,len,min_length=0.01){
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  if(length>min_length){
    fern(endpoint,initial_direction-45,length*0.38,min_length) 
    fern(endpoint,initial_direction,length*0.87,min_length)
  }
}

##### 29. fern2  dir iswhether the side branch is to the left (-1) or right (1)

fern2 <- function(starting_point,initial_direction,len,min_length=0.01,dir=1){
  
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  dir=dir*-1 # alternates between -1 and 1
  if(length>min_length){
    fern2(endpoint,initial_direction-(dir*45),length*0.38,min_length,dir) # plots alternatively right and left branches 
    fern2(endpoint,initial_direction,length*0.87,min_length,dir)
  }
  
}


# Challenge F, fern2 but with a built in timer and returns the time for different values of the shortest length
challenge_F <- function(starting_point=c(5,1),initial_direction=90,len=1,min_leng=c(0.001,0.01,0.05,0.1),dir=1){
  par(mfrow=c(2,2))
  for(i in 1:length(min_leng)){
    plot(c(0:10),c(0:10),"n",main = paste0("Minimum length = ",min_leng[i]))
    t =proc.time()
    length=len
    min_length=min_leng[i]
    endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
    dir=dir*-1 # alternates between -1 and 1
    if(length>min_length){
      fern2(endpoint,initial_direction-(dir*45),length*0.38,length,dir) # plots alternatively right and left branches 
      fern2(endpoint,initial_direction,length*0.87,min_length,dir)
    }
    time <- proc.time()-t
    print(paste0("The time taken for ",min_leng[i], " was ",time[3]," seconds"))
  }
  
}




