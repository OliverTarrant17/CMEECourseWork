#run with Rscript Visualise.R basenames

rm(list=ls())
graphics.off()
library(ggplot2)
library(RColorBrewer)
library(reshape2)
args = commandArgs(trailingOnly=TRUE)

input = args[1]
file_list <- unlist(read.table(input, header=FALSE, as.is=T))
basename_files <- c()
genolike_files <- c()
ploids_files <- c()
out_plot <- c()
win<-strtoi(args[2])

# Extract file names and build output names
for(i in 1:length(file_list)){
  genolike_files[i] <- paste(file_list[i],".genolikes.gz",sep="")
  splittedName <- unlist(strsplit(file_list[i],split="/"))
  basename_files[i] <- splittedName[length(splittedName)]
  out_plot[i] <- paste(file_list[i],"_plot.pdf",sep="")
  ploids_files[i] <- paste(file_list[i],".ploids",sep="")
} 


for(i in 1:length(file_list)){                 
  genolikes = genolike_files[i]
  ploidies = ploids_files[i]
  output = out_plot[i]

  Genolikes=read.csv(gzfile(genolikes),sep="\t",header=FALSE) # Load the data
  Ploidies=read.csv(ploidies,sep="\t",header=FALSE) # load the ploidies
  #extract the number of smaples and extract expected ploidies removing NA values
  sams<-head(Ploidies,1)
  NSAMS=length(Ploidies)-sum(is.na(sams))
  Expected_Ploidies<-tail(Ploidies,NSAMS)
  Expected_Ploidies <- Expected_Ploidies[,colSums(is.na(Expected_Ploidies))<nrow(Expected_Ploidies)]
  Ploidies<-head(Ploidies,2)
  Ploidies <- Ploidies[,colSums(is.na(Ploidies))<nrow(Ploidies)]

  Depths=Genolikes$V5
  length_of_sample=length(Depths)/NSAMS
  Ploidies_to_sum=Ploidies[1,]
  Ploidies_to_sum[is.na(Ploidies_to_sum)]<-0
  Meandepth=sum(Depths)/(length_of_sample*sum(Ploidies_to_sum))
  # create a vector of lists of depths for each sample

  sample_depths <- vector("list",NSAMS)
  for(j in 0:(NSAMS-1)){
    p=1
    for(i in 1:length(Depths)){
      if(i%%NSAMS==j){
        if(j==0){
          sample_depths[[NSAMS]][p]<-Depths[i]
          p<-p+1
        }else{
          sample_depths[[j]][p]<-Depths[i]
          p<-p+1}
      }
    }
  }

  depths <- as.data.frame(sample_depths[[1]])

  for(i in c(2:NSAMS)){
    depths<-cbind(depths,sample_depths[[i]])
  }
  col_names=c(1:NSAMS)
  colnames(depths)<-col_names


  depths <-melt(depths)

  ploidy<-c()

  for(j in Ploidies){
    ploidy<- c(ploidy,rep(j[1],length_of_sample))

  }
  depths <- cbind(depths,ploidy)

  # Add the window by window analysis
  length_of_window=win
  expected_ploidy<-c()
  excess=length_of_sample-(win*length(Expected_Ploidies))
  
  for(n in 1:NSAMS){
    for(j in Expected_Ploidies[n,]){
      expected_ploidy<- c(expected_ploidy,rep(j,length_of_window))
      }
    expected_ploidy<-c(expected_ploidy,rep(Expected_Ploidies[n,length(Expected_Ploidies)],excess))
      
      
    
    
  }
  depths <- cbind(depths,expected_ploidy)
  
  
  myColors <- mycols <- colors()[c(12,414,576,573,524,436,106,74,75,86,99,137,627,656,367,419,81,410,512,402,468,592,535,429,404,477,50,79,102,20,101,52,51,24,134,616)]
  names(myColors) <- levels(depths$variable)
  colScale <- scale_colour_manual(name = "Sample",values = myColors)



  plot<-ggplot(data = depths) + xlim(0,length(Depths)) +ylim(0,quantile(Depths,0.9)) # plot axis
  plot <- plot + theme(legend.position = "right",plot.title = element_text(hjust = 0.5))
  plot <- plot + geom_line(data=depths,aes(x=c(1:length(Depths)),y=value,colour=factor(variable))) +colScale # plot depths
  plot <- plot + ggtitle("Predicted ploidies vs depth") + ylab("Depth") # add titles
  plot <- plot + geom_line(data = depths,aes(x=c(1:length(Depths)),y=ploidy*Meandepth), size=1,colour='black') # plot inferred ploidy
  plot <- plot + geom_line(data = depths,aes(x=c(1:length(Depths)),y=expected_ploidy*Meandepth), size=0.5,colour='red') # plot inferred ploidy
  plot <- plot +scale_y_continuous('Depth',limits=c(0,Meandepth*10),sec.axis = sec_axis(~./Meandepth, name = 'Inferred Ploidy',breaks = c(0,1,2,3,4,5,6,7,8))) # add 2nd y axis
  plot <- plot + scale_x_continuous(name = "Sample", breaks = c(1:NSAMS)*length_of_sample-(length_of_sample/2),labels = c(1:NSAMS)) # change scale on x axis to samples
  

  pdf(output, 11.7, 8.3)
  plot(plot)
  graphics.off()
}
