# LAB A: Linear and exponential change
period <- 0:10
linear <- 100 + 20 * period
exponential <- 100 * 1.2^period
results <- data.frame(period, linear, exponential)
print(results)
plot(period, exponential, type = "b", col = "blue", pch = 19,
     xlab = "Period", ylab = "Amount", main = "Change models")
lines(period, linear, type = "b", col = "red", pch = 17)
legend("topleft", legend = c("Exponential", "Linear"),
       col = c("blue", "red"), lty = 1, pch = c(19, 17))
cat("At t=5:", exponential[6], "versus", linear[6], "\n")
# End laboratory A

# LAB B: Half-life and inverse calculation
C0 <- 32
k <- 0.18
target <- 5
half_life <- log(2) / k
time_to_target <- log(C0 / target) / k
check <- C0 * exp(-k * time_to_target)
print(c(half_life = half_life, time_to_target = time_to_target,
        checked_concentration = check))
# End laboratory B

# LAB C: Log-linear fitting and residual inspection
time <- c(0, 2, 4, 6, 8)
measured <- c(40, 26, 17, 10.8, 7.4)
fit <- lm(log(measured) ~ time)
intercept <- coef(fit)[1]
rate <- coef(fit)[2]
predicted <- exp(predict(fit))
residual <- measured - predicted
print(data.frame(time, measured, predicted, residual))
cat("Estimated A0:", exp(intercept), "rate:", rate, "\n")
plot(time, measured, pch = 19, xlab = "Time (hours)",
     ylab = "Concentration (mg/L)", main = "Exponential fit")
lines(time, predicted, col = "blue", lwd = 2)
plot(time, residual, pch = 19, xlab = "Time (hours)",
     ylab = "Observed - predicted", main = "Residuals")
abline(h = 0, lty = 2)
# End laboratory C
