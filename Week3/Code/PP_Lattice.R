
### Practical 9.2
rm(list = ls()) 
library(lattice) # load the lattice library
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv") # read the data set

########### Plots#############
# Predator size lattice
graphics.off() # close all previous graphics
pdf("../Results/Pred_Lattice.pdf",11.7,8.3)
 # Open blank pdf and set page size
	densityplot(~log(Predator.mass), data = MyDF, 
		xlab = "log Predator Mass (kg)", 
		ylab = "Density", main = "Predator mass",
		col="purple")
	# plots the lattice graph of log of the predators mass from MyDF,
	# with the given titles and plotted in red
	dev.off() # close the device so don't overlay plots the file

# Prey size lattice
graphics.off()
pdf("../Results/Prey_Lattice.pdf",11.7,8.3)
	densityplot(~log(Prey.mass), data = MyDF, 
		xlab = "log Prey Mass (kg)", ylab = "Density",
		main = "Prey mass",col="green")
	dev.off() # Same plotting method as above but in green
	
# Predator/Prey size ratio lattice	
graphics.off()
pdf("../Results/SizeRatio_Lattice.pdf",11.7,8.3)
	densityplot(~(log(Predator.mass/Prey.mass)), 
		data = MyDF, xlab = "Size ratio", ylab = "Density",
		main = "Predator prey size ratio", col="red")
	dev.off() # Same plotting method as above but plotting the predator mass/prey mass and plotting in red

########## PP_Results#############
### Creating a csv file of the means and medians of prey, predator masses and predator
### prey size ratio, stratified by feeding type
# mean log predator mass
log_Predator_mass_mean <- tapply(log(MyDF$Predator.mass) , MyDF$Type.of.feeding.interaction,mean) # applies the given functions to the stated data seperated by the given variables
log_Predator_mass_median <- tapply(log(MyDF$Predator.mass), MyDF$Type.of.feeding.interaction, median)
log_Prey_mass_mean <- tapply(log(MyDF$Prey.mass) , MyDF$Type.of.feeding.interaction,mean)
log_Prey_mass_median <- tapply(log(MyDF$Prey.mass), MyDF$Type.of.feeding.interaction, median)
log_Ratio_mean <- tapply((log(MyDF$Predator.mass)/log(MyDF$Prey.mass)),MyDF$Type.of.feeding.interaction,mean)
log_Ratio_median <- tapply((log(MyDF$Predator.mass)/log(MyDF$Prey.mass)),MyDF$Type.of.feeding.interaction,median)
New_DF <- data.frame(log_Predator_mass_mean,log_Predator_mass_median,log_Prey_mass_mean,log_Prey_mass_median,log_Ratio_mean,log_Ratio_median) # Creating a dataframe with the results

write.csv(New_DF,"../Results/PP_Results.csv")
