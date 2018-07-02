
## An example of using by (similar to tapply)
# import some data

attach(iris)
print(iris)

## use colMeans (as it is better for dataframes)
print(by(iris[,1:2], iris$Species, colMeans)) #prints the column means for 
#columns one and two all grouped by species
print(by(iris[,1:2], iris$Petal.Width, colMeans)) #prints the column means for 
#columns one and two all grouped by petal widths
