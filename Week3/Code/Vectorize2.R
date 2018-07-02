# Runs the stochastic (with gaussian fluctuations) Ricker Eqn .

rm(list=ls())

stochrick<-function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{ # p0 is a vector of 1000 random numbers from uniform dist between 0.5 and 1.5
  #initialize
  N<-matrix(NA,numyears,length(p0)) # N is a matrix of NA with numyears rows and len(p0) columns
  N[1,]<-p0
  
  for (pop in 1:length(p0)) #loop through the populations 
  {
    for (yr in 2:numyears) #for each pop, loop through the years
    {
      N[yr,pop]<-N[yr-1,pop]*exp(r*(1-N[yr-1,pop]/K)+rnorm(1,0,sigma))
    } # Calculate the value of the next population step 
  }
  return(N)
}

 print("Stochastic Ricker takes:")
 print(system.time(res2<-stochrick()))
# Now write another code called stochrickvect that vectorizes the above 
# to the extent possible, with improved performance: 


rm(list=ls())

stochrickvect<-function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{ # p0 is a vector of 1000 random numbers from uniform dist between 0.5 and 1.5
  #initialize
  N<-matrix(NA,numyears,length(p0)) # N is a matrix of NA with numyears rows and len(p0) columns
  N[1,]<-p0
   
  
    for (yr in 2:numyears) #for each pop, loop through the years
    {
      N[yr,]<-N[yr-1,]*exp(r*(1-N[yr-1,]/K)+rnorm(length(p0),0,sigma))
    } # Calculate the value of the next population step 
  
  return(N)

}
# Now write another code called stochrickvect that vectorizes the above 
# to the extent possible, with improved performance: 

 print("Vectorized Stochastic Ricker takes:")
 print(system.time(res2<-stochrickvect()))

 