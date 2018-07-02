rm(list=ls())
require(ggplot2)
require(knitr)
#### load examine and plot the data ####
load("../Data/KeyWestAnnualMeanTemperature.RData", verbose = TRUE)
head(ats)
str(ats)
print("The range of temperatures is: ")
print(range(ats$Temp))
print("The range of years is: ")
print(range(ats$Year))
print("The mean temperatures is: ")
print(mean(ats$Temp))
print("The median temperatures is: ")
print(median(ats$Temp))
print(ggplot(data = ats, aes(x=Year,y=Temp))+geom_line(color = "blue")+geom_point(color ="red"))


#### Correlation ####


vec1 <- ats$Temp[1:99]
vec2 <- ats$Temp[2:100]
a <- cor(vec1,vec2, method ="pearson")
correlations <- vector(mode = "numeric", length = 1000)
count <- 0
for(i in 1:10000){
  vec1 <- ats$Temp[c(sample(ats$Temp,99,replace =FALSE))]
  vec2 <- ats$Temp[c(sample(ats$Temp,99,replace=FALSE))]
  correlations[i] <- cor(vec1,vec2,method = "pearson")

}
count <- length(which(correlations>a))
    

approx_p <- count/10000
print("The correlation coefficient is: ")
print(a)
print("The approximate p-value is: ")
print(approx_p)
###### Output is formatted in a LaTex file using the TAutoCorr_Analysis.Rnw
###### file. 
#knit("TAutoCorr_Analysis.Rnw")


    
