rm(list=ls())
require(ggplot2)
for(i in c(2,5,10,25,50,100)){
  graphics.off()
  Poiss_Analysis <- as.data.frame(read.csv(paste0("../Results/First_Analysis/",i,"/Poiss_Analysis_",i,".csv"),header = TRUE),mode=numeric)
  Binom_Analysis <- as.data.frame(read.csv(paste0("../Results/First_Analysis/",i,"/Binom_Analysis_",i,".csv"),header = TRUE),mode=numeric)
  Neg_Binom_Analysis <- as.data.frame(read.csv(paste0("../Results/First_Analysis/",i,"/Neg_Binom_Analysis_",i,".csv"),header = TRUE),mode=numeric)
  
  Poiss_vals <- as.data.frame(read.csv(paste0("../Results/First_Analysis/",i,"/Poiss_Model_Vals_",i,".csv"),header = TRUE),mode=numeric)
  Binom_vals <- as.data.frame(read.csv(paste0("../Results/First_Analysis/",i,"/Binom_Model_Vals_",i,".csv"),header = TRUE),mode=numeric)
  Neg_Binom_vals <- as.data.frame(read.csv(paste0("../Results/First_Analysis/",i,"/Neg_Binom_Model_Vals_",i,".csv"),header = TRUE),mode=numeric)
  
  AIC_Poiss <- Poiss_Analysis[2]
  AIC_Binom <- Binom_Analysis[2]
  AIC_Neg_Binom <- Neg_Binom_Analysis[2]
 
    p1 <- ggplot(Poiss_vals) + geom_point(aes(x=X1,y=Actual_1)) + geom_line(aes(x=X1,y=X1_val,color=paste0("Poisson/",AIC_Poiss[1,1])),linetype="dotted")+
                                           geom_line(data=Binom_vals,aes(x=X1,y=X1_val,color=paste0("Binomial/",AIC_Binom[1,1])),linetype="dotted") +
                                           geom_line(data=Neg_Binom_vals,aes(x=X1,y=X1_val,color=paste0("Negative_Binomial/",AIC_Neg_Binom[1,1])),linetype="dotted")+ 
                       labs(title=paste0("Ploidy 1 at mean read depth ",i), x="Occurances of base",y="Frequency",color="Distribution/AIC")+
                             theme(legend.position = "right")
    
    p2 <- ggplot(Poiss_vals) + geom_point(aes(x=X2,y=Actual_2)) + geom_line(aes(x=X2,y=X2_val,color=paste0("Poisson/",AIC_Poiss[2,1])),linetype="dotted")+
      geom_line(data=Binom_vals,aes(x=X2,y=X2_val,color=paste0("Binomial/",AIC_Binom[2,1])),linetype="dotted") +
      geom_line(data=Neg_Binom_vals,aes(x=X2,y=X2_val,color=paste0("Negative_Binomial/",AIC_Neg_Binom[2,1])),linetype="dotted")+ 
      labs(title=paste0("Ploidy 2 at mean read depth ",i), x="Occurances of base",y="Frequency",color="Distribution/AIC")+
      theme(legend.position = "right")
    
    p3 <- ggplot(Poiss_vals) + geom_point(aes(x=X3,y=Actual_3)) + geom_line(aes(x=X3,y=X3_val,color=paste0("Poisson/",AIC_Poiss[3,1])),linetype="dotted")+
      geom_line(data=Binom_vals,aes(x=X3,y=X3_val,color=paste0("Binomial/",AIC_Binom[3,1])),linetype="dotted") +
      geom_line(data=Neg_Binom_vals,aes(x=X3,y=X3_val,color=paste0("Negative_Binomial/",AIC_Neg_Binom[3,1])),linetype="dotted")+ 
      labs(title=paste0("Ploidy 3 at mean read depth ",i), x="Occurances of base",y="Frequency",color="Distribution/AIC")+
      theme(legend.position = "right")
    
    p4 <- ggplot(Poiss_vals) + geom_point(aes(x=X4,y=Actual_4)) + geom_line(aes(x=X4,y=X4_val,color=paste0("Poisson/",AIC_Poiss[4,1])),linetype="dotted")+
      geom_line(data=Binom_vals,aes(x=X4,y=X4_val,color=paste0("Binomial/",AIC_Binom[4,1])),linetype="dotted") +
      geom_line(data=Neg_Binom_vals,aes(x=X4,y=X4_val,color=paste0("Negative_Binomial/",AIC_Neg_Binom[4,1])),linetype="dotted")+ 
      labs(title=paste0("Ploidy 4 at mean read depth ",i), x="Occurances of base",y="Frequency",color="Distribution/AIC")+
      theme(legend.position = "right")
    
    p5 <- ggplot(Poiss_vals) + geom_point(aes(x=X5,y=Actual_5)) + geom_line(aes(x=X5,y=X5_val,color=paste0("Poisson/",AIC_Poiss[5,1])),linetype="dotted")+
      geom_line(data=Binom_vals,aes(x=X5,y=X5_val,color=paste0("Binomial/",AIC_Binom[5,1])),linetype="dotted") +
      geom_line(data=Neg_Binom_vals,aes(x=X5,y=X5_val,color=paste0("Negative_Binomial/",AIC_Neg_Binom[5,1])),linetype="dotted")+ 
      labs(title=paste0("Ploidy 5 at mean read depth ",i), x="Occurances of base",y="Frequency",color="Distribution/AIC")+
      theme(legend.position = "right")
    
    
    pdf(paste0("../Results/First_Analysis/",i,"/Fitted_Distributions_",i,"_ploidy_1.pdf"), 11.7, 8.3)
    plot(p1)
    graphics.off()
    pdf(paste0("../Results/First_Analysis/",i,"/Fitted_Distributions_",i,"_ploidy_2.pdf"), 11.7, 8.3)
    plot(p2)
    graphics.off()
    pdf(paste0("../Results/First_Analysis/",i,"/Fitted_Distributions_",i,"_ploidy_3.pdf"), 11.7, 8.3)
    plot(p3)
    graphics.off()
    pdf(paste0("../Results/First_Analysis/",i,"/Fitted_Distributions_",i,"_ploidy_4.pdf"), 11.7, 8.3)
    plot(p4)
    graphics.off()
    pdf(paste0("../Results/First_Analysis/",i,"/Fitted_Distributions_",i,"_ploidy_5.pdf"), 11.7, 8.3)
    plot(p5)
    graphics.off()
}
