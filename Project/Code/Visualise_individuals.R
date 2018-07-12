#run with Rscript Visualise.R basenames NSAMS

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
win<-strtoi(args[3])

# Extract file names and build output names
for(i in 1:length(file_list)){ ###
  genolike_files[i] <- paste(file_list[i],".genolikes.gz",sep="")
  splittedName <- unlist(strsplit(file_list[i],split="/"))
  basename_files[i] <- splittedName[length(splittedName)]
  directory <- paste(splittedName[-length(splittedName)],collapse = '/')
  out_plot[i] <- paste(file_list[i],"_plot.pdf",sep="")
  ploids_files[i] <- paste(file_list[i],".ploids",sep="")
} 
###### Note NSAMS fixed for project work only
NSAMS=strtoi(args[2])
sam_depths <- vector("list",NSAMS)
ploidy <- vector("list",NSAMS)
length_of_samples <- c()

q=0
Exp_Ploidies <- vector("list",NSAMS*length(file_list))
for(i in 1:length(file_list)){  ###
  q=q+1
  genolikes = genolike_files[i]
  ploidies = ploids_files[i]
  output = out_plot[i]
  
  Genolikes=read.csv(gzfile(genolikes),sep="\t",header=FALSE) # Load the data
  Ploidies=read.csv(ploidies,sep="\t",header=FALSE) # load the ploidies
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
    
    if(j==0){
      sam_depths[[NSAMS]]<- append(sam_depths[[NSAMS]],sample_depths[[NSAMS]])
      ploidy[[NSAMS]] <- append(ploidy[[NSAMS]],Ploidies[[NSAMS]][1]) 
    }else{    
      sam_depths[[j]]<- append(sam_depths[[j]],sample_depths[[j]])
      ploidy[[j]] <- append(ploidy[[j]],Ploidies[[j]][1]) }
  }
  length_of_samples[q]<- length_of_sample
  
  for(sample in c(1:NSAMS)){
    for(i in c(Expected_Ploidies[sample,])){
      Exp_Ploidies[[sample+((q-1)*NSAMS)]]<-append(Exp_Ploidies[[sample+((q-1)*NSAMS)]],c(i))
    }
  }
  

}

depths <- as.data.frame(sam_depths[[1]])
  
for(i in c(2:NSAMS)){
   depths<-cbind(depths,sam_depths[[i]])
 }
col_names=c(1:NSAMS)
colnames(depths)<-col_names
   
   
depths <-melt(depths)
   
genome_length=sum(length_of_samples)
contig_num<-c()
ploidy_num<-c()
expected_ploidy<-c()
for(n in 1:NSAMS){
  
   for(i in 1:q){
     excess=length_of_samples[i]-(win*length(Exp_Ploidies[[n+(NSAMS*(i-1))]]))
     contig_num<- c(contig_num,rep(i,length_of_samples[i]))
     ploidy_num<- c(ploidy_num,rep(ploidy[[n]][i],length_of_samples[i]))
     for(j in Exp_Ploidies[[n+(NSAMS*(i-1))]]){
        expected_ploidy<-c(expected_ploidy,rep(j,win))
   }
     expected_ploidy<-c(expected_ploidy,rep(j,excess))
     
 
    }
}
depths <- cbind(depths,ploidy_num)
depths <- cbind(depths,contig_num)
depths <- cbind(depths,expected_ploidy)
   
   
   
   
myColors <- mycols <- colors()[c(12,414,576,573,524,436,106,74,75,86,99,137,627,656,367,419,81,410,512,402,468,592,535,429,404,477,50,79,102,20,101,52,51,24,134,616)]
names(myColors) <- levels(depths$contig_num)
colScale <- scale_colour_manual(name = "Contig",values = myColors)
  
for(i in 1:NSAMS){  
  output = paste0(directory,'/Sample_',i,'_plot.pdf')
  data_to_plot <- depths[depths$variable==paste0(i),]  
  Meandepth=sum(data_to_plot$value)/sum(data_to_plot$ploidy_num)
   
  plot<-ggplot(data = data_to_plot) + xlim(0,genome_length) +ylim(0,quantile(data_to_plot$value,0.8)) # plot axis
  plot <- plot + geom_jitter(data=data_to_plot,aes(x=c(1:genome_length),y=data_to_plot$value,colour=factor(contig_num))) +colScale# plot depths
  plot <- plot + ggtitle("Predicted ploidies vs depth") + ylab("Depth") # add titles
  plot <- plot + geom_line(data = data_to_plot,aes(x=c(1:length(data_to_plot$value)),y=data_to_plot$ploidy_num*Meandepth), size=1,colour='black') # plot inferred ploidy
  plot <- plot + geom_line(data = data_to_plot,aes(x=c(1:length(data_to_plot$value)),y=data_to_plot$expected_ploidy*Meandepth), size=0.5,colour='red') # plot inferred ploidy
  plot <- plot + scale_y_continuous('Depth', limits=c(0,Meandepth*10), sec.axis = sec_axis(~./Meandepth,name = 'Inferred Ploidy',breaks = c(0,1,2,3,4,5,6,7,8))) # add 2nd y axis
  plot <- plot + scale_x_continuous(name = "Contig", breaks = cumsum(length_of_samples)-length_of_samples/2,labels = c(1:max(contig_num))) # change scale on x axis to samples
   
   
  pdf(output, 11.7, 8.3)
  plot(plot)
  graphics.off()
 }
