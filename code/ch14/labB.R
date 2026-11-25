# Laboratory B: polar curves
theta <- seq(0, 2*pi, length.out=1500)
r1 <- 2*cos(3*theta); r2 <- 1+2*cos(theta)
x1 <- r1*cos(theta); y1 <- r1*sin(theta)
x2 <- r2*cos(theta); y2 <- r2*sin(theta)
par(mfrow=c(1,2))
plot(x1,y1,type="l",asp=1,col="blue",xlab="x",ylab="y",main="Three-petal rose")
plot(x2,y2,type="l",asp=1,col="red",xlab="x",ylab="y",main="Limacon with inner loop")
par(mfrow=c(1,1))
