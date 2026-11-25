# Laboratory C: periodic regression and residuals
t <- seq(0, 23, by=1); omega <- 2*pi/24
set.seed(11)
y <- 70 + 6*sin(omega*t) + 2*cos(omega*t) +
     0.12*t + rnorm(length(t), sd=0.5)
fit <- lm(y ~ sin(omega*t) + cos(omega*t))
co <- coef(fit); B <- co[2]; C <- co[3]
amp <- sqrt(B^2+C^2); phase <- atan2(C,B)
rmse <- sqrt(mean(residuals(fit)^2))
cat(sprintf("Midline=%.3f, amplitude=%.3f, phase=%.3f rad, RMSE=%.3f\n",
 co[1],amp,phase,rmse))
png("periodic_fit_R.png",width=900,height=500)
plot(t,y,pch=16,xlab="Time (hours)",ylab="Sensor reading")
lines(t,fitted(fit),col="blue",lwd=2)
dev.off()
png("periodic_residuals_R.png",width=900,height=500)
plot(t,residuals(fit),pch=16,xlab="Time (hours)",ylab="Residual")
abline(h=0,lty=2)
dev.off()
