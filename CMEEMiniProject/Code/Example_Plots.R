rm(list=ls())
require(ggplot2)
graphics.off()


##### First analysis examle plot ######
Poiss_Analysis <- as.data.frame(read.csv("../Results/First_Analysis/5/Poiss_Analysis_5.csv",header = TRUE),mode=numeric)
Binom_Analysis <- as.data.frame(read.csv("../Results/First_Analysis/5/Binom_Analysis_5.csv",header = TRUE),mode=numeric)
Neg_Binom_Analysis <- as.data.frame(read.csv("../Results/First_Analysis/5/Neg_Binom_Analysis_5.csv",header = TRUE),mode=numeric)

Poiss_vals <- as.data.frame(read.csv("../Results/First_Analysis/5/Poiss_Model_Vals_5.csv",header = TRUE),mode=numeric)
Binom_vals <- as.data.frame(read.csv("../Results/First_Analysis/5/Binom_Model_Vals_5.csv",header = TRUE),mode=numeric)
Neg_Binom_vals <- as.data.frame(read.csv("../Results/First_Analysis/5/Neg_Binom_Model_Vals_5.csv",header = TRUE),mode=numeric)

AIC_Poiss <- Poiss_Analysis[2]
AIC_Binom <- Binom_Analysis[2]
AIC_Neg_Binom <- Neg_Binom_Analysis[2]

plot1 <- ggplot(Poiss_vals) + geom_point(aes(x=X3,y=Actual_3)) + geom_line(aes(x=X3,y=X3_val,color=paste0("Poisson/",AIC_Poiss[3,1])),linetype="dotted")+
  geom_line(data=Binom_vals,aes(x=X3,y=X3_val,color=paste0("Binomial/",AIC_Binom[3,1])),linetype="dotted") +
  geom_line(data=Neg_Binom_vals,aes(x=X3,y=X3_val,color=paste0("Negative_Binomial/",AIC_Neg_Binom[3,1])),linetype="dotted")+ 
  labs(x="Occurances of base",y="Frequency",color="Distribution/AIC")+
  ggtitle("Ploidy 3 at mean read depth 5")+theme(legend.position = "right",plot.title = element_text(hjust = 0.5))


##### Second analysis example plot ####
Data <- as.data.frame(read.csv("../Results/Third_Analysis/Model_Vals_5.csv",header = TRUE),mode=numeric)
Data <- Data[-47,] # remove extra row
P <- as.data.frame(read.csv("../Results/Third_Analysis/Poisson_Confusion_data_5.csv",header=TRUE),mode=numeric)
NB <- as.data.frame(read.csv("../Results/Third_Analysis/Negative_Binomial_Confusion_data_5.csv",header = TRUE),mode=numeric)
AIC_P <- P$Minimum_value[100]
AIC_NB <- NB$Minimum_value[100]


plot2 <- ggplot(Data) + geom_point(aes(x=X,y=Actual)) + geom_line(aes(x=X,y=P_val,color=paste0("Poisson/",AIC_P)))+
  geom_line(aes(x=X,y=NB_val,color=paste0("Negative Binomial/",AIC_NB)))+labs(x="Occurances of base",y="Frequency",color="Distribution/AIC")+
  ggtitle("Mixed Ploidy genome mean depth 5")+ theme(legend.position = "right",plot.title = element_text(hjust = 0.5))

pdf("../Results/Example_Fit_Constant_Ploidy.pdf", 11.7, 8.3)
plot(plot1)
graphics.off()
pdf(paste0("../Results/Example_Fit_Mixed_Ploidy.pdf"), 11.7, 8.3)
plot(plot2)
graphics.off()

