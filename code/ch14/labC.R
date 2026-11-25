# Laboratory C: component uncertainty, reproducible simulation
set.seed(14)
n <- 2000
x <- runif(n,2.8,3.2); y <- runif(n,3.8,4.2)
magnitude <- sqrt(x^2+y^2)
cat("Nominal magnitude:",5,"\n")
cat("Simulated min/max:",range(magnitude),"\n")
cat("Componentwise theoretical bounds:",sqrt(2.8^2+3.8^2),sqrt(3.2^2+4.2^2),"\n")
plot(x,y,asp=1,pch=16,cex=.25,col="gray50",xlab="Horizontal displacement (m)",ylab="Vertical displacement (m)",main="Component uncertainty")
points(3,4,col="red",pch=19,cex=1.3)
