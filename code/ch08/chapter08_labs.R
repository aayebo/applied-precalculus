# Chapter 8: Angles, radians, and the unit circle
# Laboratory A: unit-circle coordinates
angles <- c(0, pi/6, pi/4, pi/3, pi/2, pi, 3*pi/2, 2*pi)
results <- data.frame(theta=angles, x=cos(angles), y=sin(angles))
results$identity_error <- results$x^2 + results$y^2 - 1
print(results)
theta <- seq(0, 2*pi, length.out=401)
plot(cos(theta), sin(theta), type="l", asp=1, xlab="cos(theta)", ylab="sin(theta)", main="Unit circle")
points(results$x, results$y, pch=19)

# Laboratory B: arc length and sector area
radii <- c(1, 2, 3)
angles_b <- c(pi/6, pi/3, pi/2)
model <- expand.grid(radius=radii, theta=angles_b)
model$arc_length <- model$radius * abs(model$theta)
model$sector_area <- 0.5 * model$radius^2 * abs(model$theta)
print(model)

# Laboratory C: circular motion
time <- seq(0, 4, length.out=401)
r <- 2; omega <- pi/2; phase <- pi/4
x <- r*cos(omega*time + phase)
y <- r*sin(omega*time + phase)
par(mfrow=c(1,2))
plot(time, x, type="l", ylim=c(-r,r), xlab="Time (s)", ylab="x-coordinate", main="Horizontal coordinate")
plot(x, y, type="l", asp=1, xlab="x", ylab="y", main="Circular path")
par(mfrow=c(1,1))
