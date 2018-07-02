rm(list=ls())
require(ggplot2) # Needed to produce the plots
require(reshape2)


graphics.off()
for(i in c(2,5,10,25,50,100)){
  
 ##### Load data ######
  NB_Data <- as.data.frame(read.csv(paste0("../Results/Second_Analysis/Negative_Binomial_Confusion_data_",i,".csv"),header = TRUE),mode=numeric)  # Load the outputs from the fitted models
  P_Data <- as.data.frame(read.csv(paste0("../Results/Second_Analysis/Poisson_Confusion_data_",i,".csv"),header = TRUE),mode=numeric)
  BM <- as.data.frame(read.csv(paste0("../Results/Second_Analysis/Better_Model_",i,".csv"),header = TRUE))
  
  ###### Calculate better model stats #####
  Poiss_1 <- BM$Better_Model[1:100] == "P"
  Poiss_1 = sum(Poiss_1)
  NegBinom_1 = 100-Poiss_1
  
  Poiss_2 <- BM$Better_Model[101:200] == "P"
  Poiss_2 = sum(Poiss_2)
  NegBinom_2 = 100-Poiss_2
  
  Poiss_3 <- BM$Better_Model[201:300] == "P"
  Poiss_3 = sum(Poiss_3)
  NegBinom_3 = 100-Poiss_3
  
  Poiss_4 <- BM$Better_Model[301:400] == "P"
  Poiss_4 = sum(Poiss_4)
  NegBinom_4 = 100-Poiss_4
  
  Poiss_5 <- BM$Better_Model[401:500] == "P"
  Poiss_5 = sum(Poiss_5)
  NegBinom_5 = 100-Poiss_5
  
  Poiss_T = sum(Poiss_1,Poiss_2,Poiss_3,Poiss_4,Poiss_5)
  NegBinom_T = 500-Poiss_T
  
  #### Bar Charts
  CCNV <- c(1,2,3,4,5)
  Poisson <- c(Poiss_1,Poiss_2,Poiss_3,Poiss_4,Poiss_5)
  Neg_Binom <- c(NegBinom_1,NegBinom_2,NegBinom_3,NegBinom_4,NegBinom_5)
  df <- data.frame(CCNV,Poisson,Neg_Binom)
  df_long <- melt(df, id=c("CCNV"))
  
  bar <- ggplot(df_long) + geom_bar(aes(x = CCNV, y = value, fill = variable), stat = "identity", position = "dodge", 
                             width = 0.7,color = "black") + scale_fill_manual("Distribution\n", values = c("red","blue"), 
                                                              labels = c("Poisson", "Negative Binomial")) + 
    ggtitle(paste0("Mean haploid read depth: ",i)) + labs(x="\nCCNV",y="Better Model\n") + theme_bw(base_size = 14)+theme(plot.title = element_text(hjust = 0.5))
  pdf(paste0("../Results/Second_Analysis/Better_model_bar",i,".pdf"),width=8,height=11)
  plot(bar)
  graphics.off()
  
  ##### RMSD #####
  print(paste0("Depth ",i," Poiss RMSD 1,2,3,4,5,T"))
  Poiss_1_RMSD = (sum((P_Data$Predicted[1:100]-P_Data$Actual[1:100])^2)/100)^0.5
  print(Poiss_1_RMSD)
  Poiss_2_RMSD = (sum((P_Data$Predicted[100:200]-P_Data$Actual[100:200])^2)/100)^0.5
  print(Poiss_2_RMSD)
  Poiss_3_RMSD = (sum((P_Data$Predicted[201:300]-P_Data$Actual[201:300])^2)/100)^0.5
  print(Poiss_3_RMSD)
  Poiss_4_RMSD = (sum((P_Data$Predicted[301:400]-P_Data$Actual[301:400])^2)/100)^0.5
  print(Poiss_4_RMSD)
  Poiss_5_RMSD = (sum((P_Data$Predicted[401:500]-P_Data$Actual[401:500])^2)/100)^0.5
  print(Poiss_5_RMSD)
  Poiss_T_RMSD = (sum((P_Data$Predicted-P_Data$Actual)^2)/500)^0.5
  print(Poiss_T_RMSD)
  
  print(paste0("Depth ",i," NegBinom RMSD 1,2,3,4,5,T"))
  NB_1_RMSD = (sum((NB_Data$Predicted[1:100]-NB_Data$Actual[1:100])^2)/100)^0.5
  print(NB_1_RMSD)
  NB_2_RMSD = (sum((NB_Data$Predicted[100:200]-NB_Data$Actual[100:200])^2)/100)^0.5
  print(NB_2_RMSD)
  NB_3_RMSD = (sum((NB_Data$Predicted[201:300]-NB_Data$Actual[201:300])^2)/100)^0.5
  print(NB_3_RMSD)
  NB_4_RMSD = (sum((NB_Data$Predicted[301:400]-NB_Data$Actual[301:400])^2)/100)^0.5
  print(NB_4_RMSD)
  NB_5_RMSD = (sum((NB_Data$Predicted[401:500]-NB_Data$Actual[401:500])^2)/100)^0.5
  print(NB_5_RMSD)
  NB_T_RMSD = (sum((NB_Data$Predicted-NB_Data$Actual)^2)/500)^0.5
  print(NB_T_RMSD)
##### Plot confusion matrix ####
  
  #### make sure plot always plots 1-5
  Data_for_plot_NB_pred = append(NB_Data$Predicted,c(1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5))
  Data_for_plot_NB_Act = append(NB_Data$Actual,c(1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5))
  
  Data_for_plot_P_pred = append(P_Data$Predicted,c(1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5))
  Data_for_plot_P_Act = append(P_Data$Actual,c(1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5))
  
  Confusion_NB <- table(Data_for_plot_NB_pred,Data_for_plot_NB_Act)
  Confusion_NB <- melt(Confusion_NB)
  p<-ggplot(data = Confusion_NB,
            mapping = aes(x = Data_for_plot_NB_pred,
                          y = Data_for_plot_NB_Act)) +
    geom_tile(aes(fill = value)) +
    geom_text(aes(label = sprintf("%1.0f", value-1)), vjust = 1) +
    scale_fill_gradient(low = "blue",
                        high = "red")
  p <- p + ggtitle(paste0("Negative Binomial mean depth ",i))+labs(x="Expected mixture number",y="Best fitted mixture number")+theme(plot.title = element_text(hjust = 0.5))
  
  Confusion_P <- table(Data_for_plot_P_pred,Data_for_plot_P_Act)
  Confusion_P <- melt(Confusion_P)
  q<-ggplot(data = Confusion_P,
            mapping = aes(x = Data_for_plot_P_pred,
                          y = Data_for_plot_P_Act)) +
    geom_tile(aes(fill = value)) +
    geom_text(aes(label = sprintf("%1.0f", value-1)), vjust = 1) +
    scale_fill_gradient(low = "blue",
                        high = "red")
  q <- q + ggtitle(paste0("Poisson mean depth ",i))+labs(x="Expected mixture number",y="Best fitted mixture number")+ theme(plot.title = element_text(hjust = 0.5))
  
  
  pdf(paste0("../Results/Second_Analysis/Negative_Binomial_Confusion_Matrix_",i,".pdf"),width=8,height=11)
  plot(p)
  graphics.off()
  
  pdf(paste0("../Results/Second_Analysis/Poisson_Confusion_Matrix_",i,".pdf"),width=8,height=11)
  plot(q)
  graphics.off()
  
  ##### Print out results #####
  print(paste0("Poisson is better for depth ",i," and CCNV1 in ",Poiss_1," out of 100 cases"))
  print(paste0("Negative Binomial is better for depth ",i," and CCNV1 in ",NegBinom_1," out of 100 cases"))
  print(paste0("Poisson is better for depth ",i," and CCNV2 in ",Poiss_2," out of 100 cases"))
  print(paste0("Negative Binomial is better for depth ",i," and CCNV2 in ",NegBinom_2," out of 100 cases"))
  print(paste0("Poisson is better for depth ",i," and CCNV3 in ",Poiss_3," out of 100 cases"))
  print(paste0("Negative Binomial is better for depth ",i," and CCNV3 in ",NegBinom_3," out of 100 cases"))
  print(paste0("Poisson is better for depth ",i," and CCNV4 in ",Poiss_4," out of 100 cases"))
  print(paste0("Negative Binomial is better for depth ",i," and CCNV4 in ",NegBinom_4," out of 100 cases"))
  print(paste0("Poisson is better for depth ",i," and CCNV5 in ",Poiss_5," out of 100 cases"))
  print(paste0("Negative Binomial is better for depth ",i," and CCNV5 in ",NegBinom_5," out of 100 cases"))
  print(paste0("Poisson is better for depth ",i," overall in ",Poiss_T," out of 500 cases"))
  print(paste0("Negative Binomial is better for depth ",i," overall in ",NegBinom_T," out of 500 cases"))
}