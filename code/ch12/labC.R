n <- 1:25
b <- 12
plot(NA, xlim=c(1,25), ylim=c(0,85), xlab="Measurement index", ylab="Modeled amount (mg)", main="Retention and repeated input")
for (r in c(0.7,0.85)) {
  x <- numeric(length(n)); x[1] <- 12
  for (k in 2:length(n)) x[k] <- r*x[k-1]+b
  equilibrium <- b/(1-r)
  exact <- equilibrium+(x[1]-equilibrium)*r^(n-1)
  print(data.frame(n=n[1:6], modeled=x[1:6], explicit=exact[1:6]))
  lines(n,x,type="b",pch=ifelse(r==0.7,19,17),col=ifelse(r==0.7,"blue","red"))
  abline(h=equilibrium,lty=2,col=ifelse(r==0.7,"blue","red"))
}
legend("topleft",c("r=0.70","r=0.85"),col=c("blue","red"),pch=c(19,17))
