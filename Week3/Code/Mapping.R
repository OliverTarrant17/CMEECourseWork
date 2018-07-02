rm(list = ls())
load("../Data/GPDDFiltered.RData")
str(gpdd)
head(gpdd)
require(maps)
require(mapdata)
p <- map(database = "world",regions =".",col= 3, fill =FALSE)
p <- p + points(gpdd$lat,gpdd$long, col = "blue", pch = 23, cex =0.5) 


