# Laboratory C: noisy concentration measurements
set.seed(15)
Cfun <- function(t) 10*exp(-.25*t)
t <- seq(0,8,by=.1)
y <- Cfun(t)+rnorm(length(t),mean=0,sd=.04)
dt <- diff(t)
rate <- diff(y)/dt
truth <- -.25*Cfun(t[-length(t)])
print(head(data.frame(t=t[-length(t)],observed=rate,model=truth),12))
plot(t[-length(t)],rate,type="l",xlab="time (hours)",ylab="rate (mg/L/hour)",main="Noisy rates")
lines(t[-length(t)],truth,col="red",lwd=2)
legend("bottomright",c("noisy forward differences","model rate"),col=c("black","red"),lty=1,bty="n")
