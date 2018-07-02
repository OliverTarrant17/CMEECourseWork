## run a simulation that involves sampling from a population
## script stops and returns a error message "Couldn't calculate
## mean: too few arguments!" when doit kicks code into the else 
## path

x <- rnorm(50)
doit <- function(x) {
	x <- sample(x, replace = TRUE) # takes a smaple of default length(x) elements from the sample x with replacment
	if(length(unique(x)) > 30) { # only takes mean if sample was sufficient
		print(paste("Mean of this sample was:", as.character(mean(x))))
		}
	else {
		stop("Couldn't calculate mean: too few unique points!")
	}
	}

## Run 100 iterations using vectorization:
result <- lapply(1:100, function(i) doit(x)) # creates an object i to cycle through list so that function is applied to each individually
# if not there would apply to columns 
## Or using a for loop:
result <- vector("list", 100) #Preallocate/Initialize
for(i in 1:100){
	result[[i]] <- try(doit(x),FALSE) # This allows the code to keep running
	# despite the error and returns the error message in the code
	
}
