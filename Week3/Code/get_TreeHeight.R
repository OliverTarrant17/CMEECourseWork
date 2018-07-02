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

Tree_data <- commandArgs(trailingOnly = T)

Trees <- read.csv(Tree_data[1])


TreeHeight <- function(degrees, distance){
	radians <- degrees * pi / 180
	height <- distance * tan(radians)
	print(paste("Tree height is:", height))
	
	return (height)

}

Trees$Tree.Height.m <- TreeHeight(Trees$Angle.degrees, Trees$Distance.m) # Adds a new column to Trees and for each row calculates TreeHeight for the value for this new column

name <- basename(Tree_data) ; name <- strsplit(name,".csv") # basename strips all of the path to the file, strsplit then removes the trailing .csv

write.csv(Trees, paste0("../Results/",name,"_treeheights.csv")) # writes the resulting data in an output file named using the remaining elements from previous line

	

