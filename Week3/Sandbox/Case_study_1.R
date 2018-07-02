require(ggplot2)
require(reshape2)

GenerateMatrix <- function(N) {
  M <- matrix(runif(N*N),N,N)
  return(M)
}
M <- GenerateMatrix(10)

M[1:3,1:3]
Melt <- melt(M)

Melt[1:4,]

ggplot(Melt, aes(Var1,Var2,fill=value)) +geom_tile()

p <- ggplot(Melt, aes(Var1,Var2,fill = value))
p <- p +geom_tile(colour ="black")

q <- p + theme(legend.position = "none")

q <- p + theme(legend.position = "none",
               panel.background = element_blank(),
               axis.ticks = element_blank(),
               panel.grid.major = element_blank(),
               panel.grid.minor = element_blank(),
               axis.text.x = element_blank(),
               axis.title.x = element_blank(),
               axis.text.y = element_blank(),
               axis.title.y = element_blank())

q + scale_fill_continuous(low = "yellow",
                          high = "darkgreen")
q + scale_fill_gradient2()
q + scale_fill_gradientn(colours = grey.colors(10))
q + scale_fill_gradientn(colours = rainbow(10))
q + scale_fill_gradientn(colours = c("red" "white", "blue"))