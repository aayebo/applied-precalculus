# Chapter 6 computational laboratories - run from top to bottom
# LAB A: polynomial zeros and multiplicity
p <- function(x) (x+1)*(x-2)^2
x <- seq(-3, 4, length.out=600)
plot(x, p(x), type="l", col="blue", lwd=2,
     xlab="x", ylab="P(x)", main="Polynomial zeros and multiplicity")
abline(h=0, lty=2)
points(c(-1,2), c(0,0), pch=19, col="red")
print(data.frame(zero=c(-1,2), value=p(c(-1,2))))

# LAB B: rational function and vertical asymptote
rfun <- function(x) (x+1)/(x-2)
left <- seq(-5, 1.85, length.out=300)
right <- seq(2.15, 7, length.out=300)
plot(left, rfun(left), type="l", col="blue", lwd=2,
     xlim=c(-5,7), ylim=c(-12,12), xlab="x", ylab="R(x)",
     main="Rational function with asymptotes")
lines(right, rfun(right), col="blue", lwd=2)
abline(v=2, h=1, col="red", lty=2)

# LAB C: saturation model
S <- function(c) 100*c/(10+c)
c <- seq(0,100,length.out=300)
plot(c,S(c),type="l",lwd=2,col="blue",xlab="Concentration (mg/L)",
     ylab="Signal",main="Saturation response")
abline(h=100,col="red",lty=2)
print(data.frame(concentration=c(0,10,30,40),signal=S(c(0,10,30,40))))
stopifnot(abs(S(40)-80)<1e-10)
