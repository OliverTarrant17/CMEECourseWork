rm(list=ls())
require(ggplot2)

a <- read.table("../Data/Results.txt", header = TRUE)

print(a[1:3,])
print(a[90:95,])

a$ymin <- rep(0,dim(a)[1])

p <- ggplot(a)
p <- p +geom_linerange(data=a ,
                       aes(x=x,ymin=ymin,ymax=y1,size=(0.5)),
                       colour = "#E69F00", alpha =1/2,
                       show.legend=FALSE)

p <- p + geom_linerange(data = a, aes(x=x,
                                      ymin=ymin,ymax=y2,
                                      size=(0.5)),colour="#56B4E9",
                        alpha=1/2, show.legend=FALSE)
p <- p + geom_linerange(data =a, aes(x=x,ymin=ymin, ymax=y3,
                                     size =(0.5)),colour ="#D55E00",
                        alpha =1/2, show.legend = FALSE)
p <- p +geom_text(data=a, aes(x=x,y=-500, label =Label))

p <- p + scale_x_continuous("My x axis",breaks=seq(3,5,by = 0.05)
                            ) +
  scale_y_continuous("My y axis") + theme_bw() + 
    theme(legend.position = "none")

pdf("../Results/MyBars.pdf",width =12, height = 6)
print(p)
dev.off()
