x <- 1:20 # creates a vector of 1 to 20
y <- factor(rep(letters[1:5],each = 4)) # Creates a factor of the same length with
#each letter repeated 4 times, this is defining groups
#ie aaaabbbbcccc...

print(tapply(x,y,sum)) # adds all the a's, b's ... and returns a list of the totals
# for each letter

