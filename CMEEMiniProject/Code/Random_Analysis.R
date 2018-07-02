rm(list=ls())
require(ggplot2) # Needed to produce the plots
require(reshape2)


graphics.off()
for(i in c(2,5,10,25,50,100)){
  
  ##### Load data ######
  NB_Data <- as.data.frame(read.csv(paste0("../Results/Third_Analysis/Negative_Binomial_Confusion_data_",i,".csv"),header = TRUE),mode=numeric)  # Load the outputs from the fitted models
  P_Data <- as.data.frame(read.csv(paste0("../Results/Third_Analysis/Poisson_Confusion_data_",i,".csv"),header = TRUE),mode=numeric)
  BM <- as.data.frame(read.csv(paste0("../Results/Third_Analysis/Better_Model_",i,".csv"),header = TRUE))
  Ploidies=list()
  #for(j in 1:100){
  #  temp <- as.vector(read.table(paste0("../Data/Third_Analysis/",i,"/Genome_ploidy_",j,".txt"),header = FALSE))$V1
  #  Ploidies[[j]]<- temp
  #}
  #Ploidies<-as.data.frame(Ploidies)
  #Ploidies <- t(Ploidies)
  #write.csv(Ploidies,paste0("../Results/Third_Analysis/ploidies",i,".csv"),row.names = F)
  
  ### Create predictions for genome composition from neg_Binom
  coef_1 = round(NB_Data$Coef1/0.2)
  for(m in 1:length(coef_1)){ ## Check all vaues are positive
    if(coef_1[m]<0){
      coef_1[m]=0
    }
  }
  coef_2 = round(NB_Data$Coef2/0.2)
  for(m in 1:length(coef_2)){
    if(coef_2[m]<0){
      coef_2[m]=0
    }
  }
  coef_3 = round(NB_Data$Coef3/0.2)
  for(m in 1:length(coef_3)){
    if(coef_3[m]<0){
      coef_3[m]=0
    }
  }
  coef_4 = round(NB_Data$Coef4/0.2)
  for(m in 1:length(coef_4)){
    if(coef_4[m]<0){
      coef_4[m]=0
    }
  }
  coef_5 = round(NB_Data$Coef5/0.2)
  for(m in 1:length(coef_5)){
    if(coef_5[m]<0){
      coef_5[m]=0
    }
  }
  
  Mu_1 = round(NB_Data$Mu1/i)
  Mu_2 = round(NB_Data$Mu2/i)
  Mu_3 = round(NB_Data$Mu3/i)
  Mu_4 = round(NB_Data$Mu4/i)
  Mu_5 = round(NB_Data$Mu5/i)
  
  Predicted_Ploidies<-list()
  for(k in 1:length(coef_1)){
    curve1 <- rep(Mu_1[k],coef_1[k]) 
    curve2 <- rep(Mu_2[k],coef_2[k])
    curve3 <- rep(Mu_3[k],coef_3[k]) 
    curve4 <- rep(Mu_4[k],coef_4[k])
    curve5 <- rep(Mu_5[k],coef_5[k]) 
    temp2<-c(curve1,curve2,curve3,curve4,curve5)

    Predicted_Ploidies[[k]]<-temp2
  }

  
  
  
  
  
  
  ###### Calculate better model stats #####
  Poiss <- BM$Better_Model == "P"
  Poiss = sum(Poiss)
  NegBinom = 100-Poiss
  
  
  ##### RMSD #####
  print(paste0("Depth ",i," Poiss RMSD"))
  Poiss_RMSD <- (sum((P_Data$Predicted-P_Data$Actual)^2)/100)^0.5
  print(Poiss_RMSD)

  
  print(paste0("Depth ",i," NegBinom RMSD"))
  NB_RMSD <- (sum((NB_Data$Predicted-NB_Data$Actual)^2)/100)^0.5
  print(NB_RMSD)

  
  #### make sure plot always plots 1-5
  Data_for_plot_NB_pred = append(NB_Data$Predicted,c(1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5))
  Data_for_plot_NB_Act = append(NB_Data$Actual,c(1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5))
  
  Data_for_plot_P_pred = append(P_Data$Predicted,c(1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5))
  Data_for_plot_P_Act = append(P_Data$Actual,c(1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5))
  
  
  ##### Plot confusion matrix ####
  Confusion_NB <- table(Data_for_plot_NB_pred,Data_for_plot_NB_Act)
  Confusion_NB <- melt(Confusion_NB)
  p<-ggplot(data = Confusion_NB,
            mapping = aes(x = Data_for_plot_NB_pred,
                          y = Data_for_plot_NB_Act)) +
    geom_tile(aes(fill = value-1)) +
    geom_text(aes(label = sprintf("%1.0f", value-1)), vjust = 1) +
    scale_fill_gradient(low = "blue",
                        high = "red")
  p <- p + ggtitle(paste0("Negative Binomial mean depth ",i))+labs(x="Expected mixture number",y="Best fitted mixture number")+ theme(plot.title = element_text(hjust = 0.5))
  
  Confusion_P <- table(Data_for_plot_P_pred,Data_for_plot_P_Act)
  Confusion_P <- melt(Confusion_P)
  q<-ggplot(data = Confusion_P,
            mapping = aes(x = Data_for_plot_P_pred,
                          y = Data_for_plot_P_Act)) +
    geom_tile(aes(fill = value-1)) +
    geom_text(aes(label = sprintf("%1.0f", value-1)), vjust = 1) +
    scale_fill_gradient(low = "blue",
                        high = "red")
  q <- q + ggtitle(paste0("Poisson mean depth ",i))+labs(x="Expected mixture number",y="Best fitted mixture number")+ theme(plot.title = element_text(hjust = 0.5))
  
  
  pdf(paste0("../Results/Third_Analysis/Negative_Binomial_Confusion_Matrix_",i,".pdf"),width=8,height=11)
  plot(p)
  graphics.off()
  
  pdf(paste0("../Results/Third_Analysis/Poisson_Confusion_Matrix_",i,".pdf"),width=8,height=11)
  plot(q)
  graphics.off()
  
  ##### Print out results #####
  print(paste0("Poisson is better for depth ",i," and in ",Poiss," out of 100 cases"))
  print(paste0("Negative Binomial is better for depth ",i," and in ",NegBinom," out of 100 cases"))

}
