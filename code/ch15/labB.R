# Laboratory B: one-sided limits and continuity
g <- function(x) ifelse(x<2,x+1,5-x)
for (h in c(.1,.01,.001)) {
  cat("h:",h,"left:",g(2-h),"right:",g(2+h),"\n")
}
x <- seq(0,4,length.out=401)
plot(x,g(x),type="l",lwd=2,xlab="x",ylab="g(x)",main="Piecewise continuity")
points(2,3,pch=19)
