# Chapter 4: Function tables and graphs
x <- seq(-3, 3, by=0.5)
linear <- 2*x+1; quadratic <- x^2-2*x
print(data.frame(x,linear,quadratic))
plot(x,quadratic,type="l",col="blue",lwd=2); lines(x,linear,col="red",lwd=2)
# Domain investigation
x <- seq(-4,8,length.out=500)
y <- ifelse(x>=2 & abs(x-5)>1e-8,sqrt(pmax(x-2,0))/(x-5),NA_real_)
plot(x,y,type="l",ylim=c(-4,4)); abline(v=5,lty=2)
# Secant slopes
f <- function(x) x^2
h <- c(1,.5,.1,.01,.001)
print(data.frame(h,slope=(f(2+h)-f(2))/h))
