# Laboratory C: periodic sensor and threshold times
sensor <- function(t) 2 + 0.8*sin(pi*t/3)
t <- seq(0, 12, length.out=1201)
crossings <- c(0.5, 2.5, 6.5, 8.5)
plot(t, sensor(t), type="l", col="blue", xlab="Time (seconds)", ylab="Sensor units", main="Illustrative periodic sensor")
abline(h=2.4, col="red", lty=2)
points(crossings, sensor(crossings), pch=19)
print(data.frame(time=crossings, sensor=sensor(crossings)))
