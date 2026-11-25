# Laboratory B: compare linear and exponential models
time <- 0:5
y <- c(19.8,15.0,11.7,8.7,6.8,5.2)
linear_fit <- lm(y ~ time)
exp_fit <- lm(log(y) ~ time)
linear_pred <- predict(linear_fit)
exp_pred <- exp(predict(exp_fit))
rmse <- function(actual, predicted) sqrt(mean((actual-predicted)^2))
print(c(linear=rmse(y,linear_pred), exponential=rmse(y,exp_pred)))
plot(time,y,xlab="Time (hours)",ylab="Measurement (units)")
lines(time,linear_pred,col="blue")
lines(time,exp_pred,col="red")
legend("topright",legend=c("Linear","Exponential"),col=c("blue","red"),lty=1)
