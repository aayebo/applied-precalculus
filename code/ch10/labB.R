# Laboratory B: solving sin(x) = 1/2 numerically
f <- function(x) sin(x) - 0.5
x <- seq(0, 4*pi, length.out=2001)
plot(x, sin(x), type="l", col="blue", xlab="x (radians)", ylab="y", main="Sine and target threshold")
abline(h=0.5, col="red", lty=2)
roots <- c(pi/6, 5*pi/6, 13*pi/6, 17*pi/6)
points(roots, sin(roots), pch=19)
print(data.frame(root=roots, residual=f(roots)))
