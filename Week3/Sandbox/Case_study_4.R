rm(list = ls())
require(ggplot2) # load package

# create an "ideal" linear regression data!
x <- seq(0,100, by = 0.1)
y <- -4. + 0.25 * x + rnorm(length(x), mean = 0., sd = 2.5)

# now a dataframe
my_data <- data.frame(x = x, y= y)

# perform a linear regression
my_lm <- summary(lm(y~x , data = my_data)) # provides residuals, and coefficients information

# plot the data
p <- ggplot(my_data, aes(x=x, y=y, colour = abs(my_lm$residuals))
            )+ geom_point() +
  scale_color_gradient(low = "black", high = "red") +
  theme(legend.position = "none") +
  scale_x_continuous(expression(alpha^2 * pi / beta * sqrt(Theta)))
# plots a scatter graph of x aggainst y with colour gradient of the 
# absolute value of resiuduals with low values in black and high in red
# no legend and x axis labeled as above

# add the regression line
p <- p + geom_abline(
  intercept = my_lm$coefficients[1][1],
  slope = my_lm$coefficients[2][1],
  colour = "yellow")

# adds the abline using vaues from the linear model coefficients

# throw some math on the plot
p <- p + geom_text(aes(x =60, y = 0, label = "sqrt(alpha) *2 * pi"),
                   parse = TRUE, size = 6,
                   colour = "blue")
# adds the lable to the graph at the stated posion in the stated size
# and stated colour

# print in a pdf
pdf("../Results/MyLinReg.pdf")
print(p)
dev.off()