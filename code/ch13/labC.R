set.seed(13)
t <- seq(0,2*pi,length.out=80)
a <- 4; b <- 2
r <- 1+rnorm(length(t),0,0.04)
x <- a*r*cos(t); y <- b*r*sin(t)
radial_residual <- sqrt((x/a)^2+(y/b)^2)-1
par(mfrow=c(1,2))
plot(x,y,asp=1,pch=19,cex=0.5,main="Simulated measurements")
lines(a*cos(seq(0,2*pi,length.out=300)),b*sin(seq(0,2*pi,length.out=300)),col="blue")
plot(t,radial_residual,pch=19,cex=0.5,main="Normalized radial residuals")
abline(h=0,lty=2);par(mfrow=c(1,1))
print(summary(radial_residual))
