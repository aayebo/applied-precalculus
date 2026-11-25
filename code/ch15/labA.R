# Laboratory A: secant slopes and tangent estimates
f <- function(x) x^2 + 3*x
a <- 2
h <- c(1, .5, .1, .01, -.01, -.1, -.5)
result <- data.frame(h=h, secant=(f(a+h)-f(a))/h, exact=2*a+h+3)
print(result)
x <- seq(-1,4,length.out=300)
plot(x,f(x),type="l",lwd=2,xlab="x",ylab="f(x)",main="Secant to tangent")
lines(x,f(a)+7*(x-a),col="red",lwd=2)
points(a,f(a),pch=19)
legend("topleft",c("f(x)","tangent"),col=c("black","red"),lty=1,bty="n")
