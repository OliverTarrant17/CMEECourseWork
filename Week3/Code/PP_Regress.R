rm(list = ls())
require(ggplot2)
require(plyr) # load packages

Data <- read.csv("../Data/EcolArchives-E089-51-D1.csv") # loads the data
############# Plotting the figure #############



p <- ggplot(Data, aes(x=Prey.mass, y =Predator.mass, colour = Predator.lifestage))
p <- p + geom_point(shape=I(3)) # plotting the points
p <- p + facet_grid(Type.of.feeding.interaction ~.) # seperate plot into different feeding interactions
p <- p + theme(legend.position = "bottom") # plots legend at the bottom
p <- p + theme(legend.title = element_text(face="bold"))# Makes legend title bold
p <- p + scale_x_continuous("Prey mass in grams", trans = "log10") + 
  scale_y_continuous("Predator mass in grams", trans = "log10")
#plotting the axis
p <- p + theme(panel.background = element_rect(fill = "white", colour = "black"), 
               panel.grid.major = element_line(colour = "grey"))
# Sorts out background and gridlines
p <- p + theme(axis.text = element_text(face = "bold")) # Makes axis text bold
p <- p + geom_smooth(method= "lm", fullrange=TRUE) # plots regression lines


pdf("../Results/Pred_Prey_Regress.pdf", 11.7, 8.3)
print(p)
dev.off()

########### Regression results ###########
my_lm <- lm(log(Predator.mass)~log(Prey.mass)*Type.of.feeding.interaction*Predator.lifestage, data = Data)
# provides a linear model of log pred mass against log prey mass
# * feeding interaction and lifestage
sum <- summary(my_lm)
a <- sum$coefficients
b <- my_lm$terms
c <- sum$fstatistic

my_lm <- function(x){
  lm(log(Predator.mass)~log(Prey.mass), data = x)
} # defines a linear model between Pred mass and Prey mass from the specified data x
fitted.model <- dlply(Data, .(Type.of.feeding.interaction, Predator.lifestage), my_lm)
# applies the model() to all subsets of Data, these have been seperated by Type.of.feeding.interaction and 
# predator.lifestage
# R squared calculator
R_sqr <- function(x) {
  summary(x)$r.squared
}
# f statistics calculator
f_stat <- function(x) {
  summary(x)$fstatistic
}
# p value calculator
p_val <- function(x){
  anova(x)$'Pr(>F)'[1]
}


a = ldply(fitted.model, coef) # returns all the coefficients from the fitted model
b = ldply(fitted.model, R_sqr) 
c = as.data.frame(ldply(fitted.model, f_stat))
d = ldply(fitted.model, p_val )
e <- merge.data.frame(a,b) # Create a data frame with the statistics
f <- merge.data.frame(e,c ,all = TRUE, check.names = TRUE) 
f <- f[1:6] # remove unwanted degrees of freedom information from f_statistic
g <- cbind(f,d[,3])
New_DF <- data.frame(g) # Name the data frame
colnames(New_DF) <- c("Feeding_Interaction", "Predator_lifestage","Intercept",
                      "Slope","R_Squared","F_statistic",
                      "P_Value")
# Added the column names wanted in the data frame

write.csv(New_DF, "../Results/PP_Regress_Results.csv") # Outputs the regression statistics in a csv file
