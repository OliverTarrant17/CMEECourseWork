### Script which takes fit data from Fitting.py and plots the resulting fits.
### Run from the terminal as follows:
### Rscript --vanilla Plotting.R [input file name with path] [bamlist.txt]
### Input file will be the output file from running Fitting.py
### Outputs pdf files of line graphs with the optimal distributions plotted over the raw data 
### Output files saved as [input file]_[sample_name]_plot.pdf for i = 1:[number of samples]



rm(list=ls())
require(ggplot2)
graphics.off()

args = commandArgs(trailingOnly=TRUE)
input = args[1]
BAMS = args[2]
bams <- as.data.frame(read.csv(BAMS,header=FALSE))
b2 <- as.vector(bams$V1) # Generate a list of the bam files from the bamlist
b<-b2
for(bam in 1:length(b)){
  b2[bam]<-unlist(strsplit(b[bam],split=".indelRealigned"))[1]
}
NSAMS = length(b) # Extract length of bamlist

NB_Data <- as.data.frame(read.csv(paste0(input,'_Negative_Binomial_data.csv'),header = TRUE),mode=numeric)
P_Data <- as.data.frame(read.csv(paste0(input,'_Poisson_data.csv'),header = TRUE),mode=numeric)
NB_AIC <- NB_Data$Minimum_AIC_value
P_AIC <- P_Data$Minimum_AIC_value
for(i in c(1:NSAMS)){
  cat(paste0("Plotting sample: ",i))
  Data <- as.data.frame(read.csv(paste0(input,"_Model_Vals_sample_",b[i],".csv"),header = TRUE),mode=numeric)
  
  
  plot1 <- ggplot(Data) + geom_point(aes(x=X,y=Actual)) + 
    geom_line(aes(x=X,y=Best.Poisson,color=paste0("Poisson/",P_AIC[i])),linetype="solid")+
    geom_line(aes(x=X,y=Best.NB,color=paste0("Negative Binomial/",NB_AIC[i])),linetype="solid") +
    ##### Uncomment lines below to view overlayed plots of other mixture models fitted to the data
    #geom_line(aes(x=X,y=Neg.Binom.1,color=paste0("Negative Binomial 1")),linetype="dotted") +
    #geom_line(aes(x=X,y=Neg.Binom.2,color=paste0("Negative Binomial 2")),linetype="dotted") +
    #geom_line(aes(x=X,y=Neg.Binom.3,color=paste0("Negative Binomial 3")),linetype="dotted") +
    #geom_line(aes(x=X,y=Neg.Binom.4,color=paste0("Negative Binomial 4")),linetype="dotted") +
    #geom_line(aes(x=X,y=Neg.Binom.5,color=paste0("Negative Binomial 5")),linetype="dotted") +
    #geom_line(aes(x=X,y=Poiss.1,color=paste0("Poisson 1")),linetype="dotted") +
    #geom_line(aes(x=X,y=Poiss.2,color=paste0("Poisson 2")),linetype="dotted") +
    #geom_line(aes(x=X,y=Poiss.3,color=paste0("Poisson 3")),linetype="dotted") +
    #geom_line(aes(x=X,y=Poiss.4,color=paste0("Poisson 4")),linetype="dotted") +
    #geom_line(aes(x=X,y=Poiss.5,color=paste0("Poisson 5")),linetype="dotted") +
    labs(x="Occurances of base",y="Frequency",color="Distribution/AIC")+
    ggtitle(paste0("Fitted distribution sample ",b2[i]))+
    theme(legend.position = "top",plot.title = element_text(hjust = 0.5,size=32,face="bold"),axis.text=element_text(size=28),axis.title = element_text(size=32,face="bold"),legend.text = element_text(size=20),legend.title = element_text(size=24))
  
  pdf(paste0(input,"_sample_",b[i],"_plot.pdf"), 11.7, 8.3)
  plot(plot1)
  graphics.off()
  cat(paste0("Sample ",i," plotted"))
}
