# Laboratory A: linear calibration and residuals
concentration <- 0:5
signal <- c(1.2, 3.0, 5.1, 6.9, 9.2, 10.8)
fit <- lm(signal ~ concentration)
prediction <- predict(fit)
residual <- signal - prediction
rmse <- sqrt(mean(residual^2))
print(coef(fit)); print(rmse)
par(mfrow=c(1,2))
plot(concentration, signal, xlab="Concentration (mg/L)", ylab="Signal (units)")
abline(fit, col="blue")
plot(concentration, residual, xlab="Concentration (mg/L)", ylab="Residual")
abline(h=0, lty=2)
par(mfrow=c(1,1))
