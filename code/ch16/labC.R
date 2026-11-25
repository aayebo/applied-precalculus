# Laboratory C: periodic model sensitivity
time <- seq(0,48,by=3)
y <- 70+8*sin(2*pi*(time-3)/24)+0.7*cos(0.8*time)
nominal <- 70+8*sin(2*pi*(time-3)/24)
print(sqrt(mean((y-nominal)^2)))
plot(time,y,xlab="Time (hours)",ylab="Signal (units)",ylim=c(60,80))
dense <- seq(0,48,length.out=400)
for (period in c(22,24,26)) {
  lines(dense,70+8*sin(2*pi*(dense-3)/period),lty=which(c(22,24,26)==period))
}
legend("topright",legend=c("22 h","24 h","26 h"),lty=1:3)
