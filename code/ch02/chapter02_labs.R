# Laboratory A
a <- 3; b <- -4; c0 <- -2
D <- b^2 - 4*a*c0
roots <- c((-b - sqrt(D))/(2*a),
           (-b + sqrt(D))/(2*a))
f <- function(x) a*x^2 + b*x + c0
print(data.frame(root=roots, residual=f(roots)))
x <- seq(-1.5, 3, length.out=400)
plot(x, f(x), type="l", lwd=2, col="steelblue",
     xlab="x", ylab="3x^2 - 4x - 2")
abline(h=0, lty=2)
points(roots, f(roots), pch=19, col="firebrick")

# Laboratory B
t <- seq(0, 8, length.out=401)
g <- (t - 2)*(t - 6)
plot(t, g, type="l", lwd=2, col="steelblue",
     xlab="Time (hours)", ylab="(t - 2)(t - 6)")
abline(h=0, lty=2)
idx <- which(g <= 0)
points(t[idx], g[idx], pch=16, cex=0.35,
       col="darkgreen")
abline(v=c(2,6), lty=3)
print(range(t[idx]))

# Laboratory C
f <- function(x) x^3 - x - 1
left <- 1; right <- 2
stopifnot(f(left)*f(right) < 0)
for (k in 1:25) {
  mid <- (left + right)/2
  if (f(left)*f(mid) <= 0) right <- mid
  else left <- mid
}
root <- (left + right)/2
cat("root =", root, "residual =", f(root),
    "width =", right-left, "\n")
