M <- matrix(runif(1000000),1000,1000) # 1000 x 1000 matrix of random uniform variables

SumAllElements <- function(M){
	Dimensions <- dim(M)
	Tot <- 0
	for (i in 1:Dimensions[1]){
		for (j in 1:Dimensions[2]){
			Tot <- Tot + M[i,j]
		}
	}
	return (Tot)
}

## This should take about a second
print("The non-vectorized version takes this long: ")
print (system.time(SumAllElements(M)))
## While this takes about 0.01 seconds
print("The vectorized version takes this long: ")
print  (system.time(sum(M)))
