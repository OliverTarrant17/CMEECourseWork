
rm(list = ls())
graphics.off()

#### Fractals in nature questions

##### 21. Fractal dimensions. Formula is  D= log(N)/log(r) where N is the number of smaller objects in the iteration and r is the size ratio from a zero iteration
##### so for the Sierpinski carpet D=log(8)/log(3) = 1.892789... and for Menger sponge D=log(20)/log(3) = 2.726833...

##### 22. The chaos game

chaos_game <- function(repeats=100){
  a <- c(0,0) ; b <- c(3,4) ; c <- c(4,1) # set the corners for the triangle
  X <- c(0,0) # set an initial start point
  plot(X[1],X[2],type="p", col ="black", cex=0.2, xlim = c(-1,5),ylim = c(-1,5)) #plot the start point small
  randoms <- runif(repeats,min=0,max=3) # generate the a rendom selection from the points the number of times that repeats is
  for(i in 1:repeats){
    if(randoms[i]<=1){
      dir=a
    }else if((randoms[i]>1)&(randoms[i]<=2)){
      dir=b
    }else if(randoms[i]>2){
      dir=c
    }
    X=(X+dir)/2 # move the point half way to the choosen point
    lines(X[1],X[2],type = "p",col="black",cex=0.2) #draw the new point
  }
}

##### Challeneg E, Allows you to specify the 3 corners for the triangle and initial start point

challenge_E <- function(initial_X=c(0,0),repeats=100,coloured=20,a=c(0,0),b=c(3,4),c=c(4,12)){
  X <- initial_X
  plot(X[1],X[2],type="p", col ="red", cex=0.2, xlim = c(-1,5),ylim = c(-1,5)) #plot the start point small
  a=a;b=b;c=c
  randoms <- runif(repeats,min=0,max=3) # generate the a rendom selection from the points the number of times that repeats is
  for(i in 1:repeats){
    if(randoms[i]<=1){
      dir=a
    }else if((randoms[i]>1)&(randoms[i]<=2)){
      dir=b
    }else if(randoms[i]>2){
      dir=c
    }
    X=(X+dir)/2 # move the point half way to the choosen point
    if(i < coloured){
       lines(X[1],X[2],type = "p",col="red",cex=0.2)
    }else{
     lines(X[1],X[2],type = "p",col="black",cex=0.2) #draw the new point
    }
  }
  
}


##### 23. Turtle,  direction taken in degrees clockwise with 0 radians being horizontal right going anticlockwise. Note direction in radians not degrees

turtle <- function(start_position,direction,length){
  endpoint_x <- start_position[1]+length*cos(direction) # calculate the endpoints for the line converting between radians and degrees
  endpoint_y <- start_position[2]+length*sin(direction)
  endpoint <- c(endpoint_x,endpoint_y)
  segments(x0=start_position[1],y0=start_position[2],x1=endpoint_x,y1=endpoint_y,col="dark green")
  return(endpoint)
}

##### 24. Elbow, two iterations of turtle, changing angle by 45 degrees clockwise and making length 0.95 original length for second iteration

elbow <- function(starting_point,initial_direction,len){
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,length = len) 
  turtle(start_position = endpoint,direction=initial_direction-45,length=0.95*len)
}

##### 25. Spiral # creates a spiral by repeating elbow. However, runs with an erroo as creates an infinite loop

spiral <- function(starting_point,initial_direction,len){ 
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,length = len)
  spiral(endpoint,initial_direction-45,0.95*len)
}

##### 26. Spiral 2 # solves the infinite loop in spiral and creates a spiral until the line length is shorter than the specified value min_length

spiral2 <- function(starting_point,initial_direction,len,min_length=0.01){
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  if(length>min_length){
    length = (length*0.95)
    spiral2(endpoint,initial_direction-45,length,min_length)
    
  }
}

###### 27. tree 

tree <- function(starting_point,initial_direction,len,min_length=0.01){
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  if(length>min_length){ # check line length is still big enough
    length = (length*0.65) # shortens line
    tree(endpoint,initial_direction-45,length,min_length)  # plots spirallig to the right
    tree(endpoint,initial_direction+45,length,min_length) # plots spiralling to the left
    
  }

}

###### 28. fern 

fern <- function(starting_point,initial_direction,len,min_length=0.01){
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  if(length>min_length){
    fern(endpoint,initial_direction-45,length*0.38,min_length) 
    fern(endpoint,initial_direction,length*0.87,min_length)
  }
}

##### 29. fern2  dir iswhether the side branch is to the left (-1) or right (1)

fern2 <- function(starting_point,initial_direction,len,min_length=0.01,dir=1){
  
  length=len
  endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
  dir=dir*-1 # alternates between -1 and 1
  if(length>min_length){
    fern2(endpoint,initial_direction-(dir*45),length*0.38,min_length,dir) # plots alternatively right and left branches 
    fern2(endpoint,initial_direction,length*0.87,min_length,dir)
  }
  
}


# Challenge F, fern2 but with a built in timer and returns the time for different values of the shortest length
challenge_F <- function(starting_point=c(5,1),initial_direction=90,len=1,min_leng=c(0.001,0.01,0.05,0.1),dir=1){
  par(mfrow=c(2,2))
  for(i in 1:length(min_leng)){
    plot(c(0:10),c(0:10),"n",main = paste0("Minimum length = ",min_leng[i]))
    t =proc.time()
    length=len
    min_length=min_leng[i]
    endpoint <- turtle(start_position = starting_point,direction = initial_direction,len)
    dir=dir*-1 # alternates between -1 and 1
    if(length>min_length){
      fern2(endpoint,initial_direction-(dir*45),length*0.38,length,dir) # plots alternatively right and left branches 
      fern2(endpoint,initial_direction,length*0.87,min_length,dir)
    }
    time <- proc.time()-t
    print(paste0("The time taken for ",min_leng[i], " was ",time[3]," seconds"))
  }
  
}



