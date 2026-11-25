# Chapter 5: Applied Precalculus — sequential R laboratories

# LAB A: TRANSFORMATIONS
x <- seq(-4, 6, length.out=500)
f <- function(x) x^2
plot(x, f(x), type="l", lwd=2, col="blue", ylim=c(-4,12),
     xlab="x", ylab="Output", main="Function transformations")
lines(x, -2*f(x-2)+5, col="red", lwd=2)
legend("topright", c("x^2", "-2(x-2)^2+5"),
       col=c("blue", "red"), lty=1, lwd=2)

# LAB B: COMPOSITION AND DOMAINS
f <- function(x) sqrt(x)
g <- function(x) 3 - x^2
x <- seq(-2, 2, length.out=401)
y <- rep(NA_real_, length(x))
valid <- g(x) >= 0
y[valid] <- f(g(x[valid]))
plot(x, y, type="l", lwd=2, col="blue",
     xlab="x", ylab="f(g(x))",
     main="Composite function with restricted domain")
print(c(-sqrt(3), sqrt(3)))

# LAB C: INVERSE CALIBRATION
signal <- function(c) 0.8*c + 2
inverse <- function(s) (s-2)/0.8
c <- seq(0, 20, length.out=101)
s <- signal(c)
plot(c, s, type="l", col="blue", lwd=2,
     xlab="Concentration (mg/L)", ylab="Signal (mV)")
print(data.frame(signal=c(2,6,10,18),
                 concentration=inverse(c(2,6,10,18))))
stopifnot(all(abs(inverse(signal(c))-c) < 1e-10))
