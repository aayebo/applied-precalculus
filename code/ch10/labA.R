# Laboratory A: identities and numerical precision
x <- seq(-2*pi, 2*pi, length.out = 1001)
pythagorean_error <- sin(x)^2 + cos(x)^2 - 1
double_angle_error <- sin(2*x) - 2*sin(x)*cos(x)
cat("Max Pythagorean error:", max(abs(pythagorean_error)), "\n")
cat("Max double-angle error:", max(abs(double_angle_error)), "\n")
plot(x, pythagorean_error, type="l", col="blue", xlab="Angle (radians)", ylab="Numerical difference", main="Floating-point identity check")
abline(h=0, lty=2)
