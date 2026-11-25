# Laboratory A: Sine and cosine transformations
x <- seq(-2*pi, 2*pi, length.out=600)
f <- 2*sin(3*(x-pi/6))+1
plot(x, f, type="l", col="blue", lwd=2,
     xlab="x (radians)", ylab="f(x)", main="Transformed sine")
abline(h=1, lty=2)
cat("Amplitude:", 2, "Period:", 2*pi/3, "Midline:", 1, "\n")
# Five key points, one cycle
key_x <- pi/6 + (0:4)*(2*pi/3)/4
key_y <- 2*sin(3*(key_x-pi/6))+1
print(data.frame(x=key_x, y=key_y))
# Save a portable image
png("chapter09_transformation_R.png")
plot(x, f, type="l", lwd=2, xlab="x", ylab="f(x)")
abline(h=1,lty=2)
dev.off()

# Laboratory B: tangent and reciprocal graphs
x <- seq(-2*pi,2*pi,length.out=3000)
tan_y <- tan(x)
sec_y <- 1/cos(x)
tan_y[abs(cos(x)) < 0.035] <- NA
sec_y[abs(cos(x)) < 0.035] <- NA
png("chapter09_reciprocal_R.png")
plot(x,tan_y,type="l",ylim=c(-4,4),col="blue",
     xlab="x (radians)",ylab="y",main="Tangent and secant")
lines(x,sec_y,col="red")
legend("topright",c("tangent","secant"),col=c("blue","red"),lty=1)
dev.off()
cat("Tangent asymptotes: pi/2 + k*pi\n")
# Excluded points are not zero values
print(c(tan(pi/4), 1/cos(pi/3)))

# Laboratory C: fit a sinusoidal model
set.seed(9)
t <- seq(0,24,by=1)
observed <- 37 + 0.4*cos(2*pi*(t-4)/24) + rnorm(length(t),0,0.06)
fit <- lm(observed ~ cos(2*pi*t/24) + sin(2*pi*t/24))
pred <- predict(fit)
residual <- observed - pred
print(summary(fit))
cat("RMSE:",sqrt(mean(residual^2)),"\n")
png("chapter09_model_R.png")
plot(t,observed,pch=19,xlab="Time (hours)",ylab="Temperature (C)")
lines(t,pred,col="blue",lwd=2)
dev.off()
