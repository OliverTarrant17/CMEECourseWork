# This function calculates heights of trees from the angle of
# elevation and the distance from the base using triginometric
# formula height = distance * tan(radians)
#
# ARGUMENTS:
# degrees 	The angle of elevation
# distance  The distance from base
#
# OUTPUT:
# The height of the tree, same units as "distance"

TreeHeight <- function(degrees, distance){
	radians <- degrees * pi / 180
	height <- distance * tan(radians)
	print(paste("Tree height is:", height))
	
	return (height)
}

Trees <- read.csv("../Data/trees.csv", header = T) # opens the CSV
Trees$Tree.Height.m <- TreeHeight(Trees$Angle.degrees, Trees$Distance.m) # Adds a new column to Trees and for each row calculates TreeHeight for the value for this new column
write.csv(Trees, "../Results/TreeHts.csv") # writes the resulting data in an output file

	

