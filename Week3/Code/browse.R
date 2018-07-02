Exponential <- function(N0 = 1, r = 1, generations = 10) {
	# Runs a simulation of exponential growth
	# Returns a vector of length generation
	
	N <- rep(NA, generations)  # Creates a vector of NA
	
	N[1] <- N0
	for (t in 2:generations) {
		N[t] <- N[t-1] * exp(r)
			browser() #stops the function at this point
			# can then evaluate all variables and can step through the 
			# rest of the script
	}
	return (N)
}
plot(Exponential(),type="l",main="Exponential growth")
