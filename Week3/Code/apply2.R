
SomeOperation <- function(v) { #This function checks if the input is greater
							   # than 0 and if it is returns 100*the input
	if (sum(v) > 0){
		return (v * 100)
	}
	return (v)
}

M <- matrix(rnorm(100), 10,10)
print (apply(M,1, SomeOperation))
# The apply function here is summing each row of the matrix
# if the row is > 0 then it applies SomeOperation to each element
# of the row and returns it as a column. If the sum is < 0 then the 
# row is just returned as a column by itself
