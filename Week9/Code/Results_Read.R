
rm(list=ls())
graphics.off()
# My unique speciation rate = 0.004361
sum_vec <- function(x=c(0,0,0),y=c(0,0,0)){
  diff <- length(x)-length(y)
  zeros <- rep(0,abs(diff)) # create a vector of zeros to add to the shorter vector
  if(diff<0){ 
    x<-append(x,zeros)   # append the zeros vector to the shorter vector
  }else{ y<-append(y,zeros)}
  return(x+y)
}

question_20 <- function(){
  oct_500 <- (0) # set initial blank vectors and counts to zero
  oct_1000 <- (0)
  oct_2500 <- (0)
  oct_5000 <- (0)
  count_500 <- 0
  count_1000 <- 0
  count_2500 <- 0
  count_5000 <- 0

  for(i in 1:100){
    load(paste0("../Results/Results",i,".rda")) # load each file in turn
    cut <- ceiling(parameters$Burn_in_Generations/parameters$Interval_Octave) # calculate the burn in period for the open file
    if((parameters$Size)==500){  #### check the population size for each file
       for(j in cut:length(octs)){
        oct_500 <- sum_vec(oct_500,unlist(octs[j])) # add all the octaves recorded past the burn in period to the vector corresponding to the octaves for the correct population size
        count_500 <- count_500+1 # Increase the count for the population size by 1 for each octave you add to the vector
        }
    }
    else if(parameters$Size==1000){
       for(j in cut:length(octs)){
         oct_1000 <- sum_vec(oct_1000,unlist(octs[j]))
         count_1000 <- count_1000+1
      }
    }
    else if(parameters$Size==2500){
       for(j in cut:length(octs)){
         oct_2500 <- sum_vec(oct_2500,unlist(octs[j]))
         count_2500 <- count_2500+1
      }
    }
    else if(parameters$Size==5000){
       for(j in cut:length(octs)){
         oct_5000 <- sum_vec(oct_5000,unlist(octs[j]))
         count_5000 <- count_5000+1
      }
    }

    }  
    oct_500_mean <- oct_500/count_500   # calculate the mean octave for each population size by using the summed vector and count
    oct_1000_mean <- oct_1000/count_1000
    oct_2500_mean <- oct_2500/count_2500
    oct_5000_mean <- oct_5000/count_5000

cat("The mean octave for 500 is: ")  # print out the mean vectors
print(oct_500_mean)
cat("The mean octave for 1000 is: ")
print(oct_1000_mean)
cat("The mean octave for 2500 is: ")
print(oct_2500_mean)
cat("The mean octave for 5000 is: ")
print(oct_5000_mean)
par(mfrow=c(2,2)) # open a plotting window split into 4 boxes
xx<-barplot(oct_500_mean, main = "Mean species abundancies over 11.5 hours for population of 500", xlab="Octave",ylab="Mean abundance",
        ylim=c(0,max(oct_500_mean)+1),col=c("red","magenta","blue","yellow","green","orange","cyan","purple","brown"),
        names.arg = c("1","2","3","4","5","6","7","8","9"), axes=TRUE)  # plot the bar chart for each mean octave
text(x=xx,y=oct_500_mean,label = oct_500_mean,pos=3,cex=0.4,col="black" ) # add the values ontop of the bars
xy<-barplot(oct_1000_mean, main = "Mean species abundancies over 11.5 hours for population of 1000", xlab="Octave",ylab="Mean abundance",
        ylim=c(0,max(oct_1000_mean)+1),col=c("red","magenta","blue","yellow","green","orange","cyan","purple","brown","grey"),
        names.arg = c("1","2","3","4","5","6","7","8","9","10"), axes=TRUE)
text(x=xy,y=oct_1000_mean,label = oct_1000_mean,pos=3,cex=0.4,col="black" )
yx<-barplot(oct_2500_mean, main = "Mean species abundancies over 11.5 hours for population of 2500", xlab="Octave",ylab="Mean abundance",
        ylim=c(0,max(oct_2500_mean)+1),col=c("red","magenta","blue","yellow","green","orange","cyan","purple","brown","grey","navy"),
        names.arg = c("1","2","3","4","5","6","7","8","9","10","11"), axes=TRUE)
text(x=yx,y=oct_2500_mean,label = oct_2500_mean,pos=3,cex=0.4,col="black" )
yy<-barplot(oct_5000_mean, main = "Mean species abundancies over 11.5 hours for population of 5000", xlab="Octave",ylab="Mean abundance",
        ylim=c(0,max(oct_5000_mean)+1),col=c("red","magenta","blue","yellow","green","orange","cyan","purple","brown","grey","navy"),
        names.arg = c("1","2","3","4","5","6","7","8","9","10","11"), axes=TRUE)
text(x=yy,y=oct_5000_mean,label = oct_5000_mean,pos=3,cex=0.4,col="black" )
}
