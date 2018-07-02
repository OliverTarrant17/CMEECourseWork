rm(list=ls())
require(ggplot2)
graphics.off()

input=args[1]

data=read.csv(input,header = F, sep = '\t',stringsAsFactors = F)
data$V4 = as.character(substr(data$V4,1,nchar(data$V4)-1))
data$V4 = as.character(substr(data$V4,2,nchar(data$V4)))

for (i in 1:length(data$V4)){
  vec=c()
  temp<-((strsplit(data$V4[i],split=',')[[1]]))
  for (j in 1:length(temp)){
    vec<-list(c(vec,as.numeric(temp[j]))) ## not working
  }
  data$V4[i]<-vec
}

