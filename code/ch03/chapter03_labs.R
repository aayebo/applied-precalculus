# Chapter 3: Laboratory A - calibration
concentration <- c(2,8)
signal <- c(9,27)
m <- diff(signal)/diff(concentration)
b <- signal[1]-m*concentration[1]
print(c(slope=m, intercept=b, signal_at_5=m*5+b))
png('chapter03_calibration_R.png')
plot(concentration,signal,pch=19,xlim=c(0,12),ylim=c(0,40),xlab='Concentration (mg/L)',ylab='Signal (units)')
abline(a=b,b=m,col='blue',lwd=2)
abline(v=c(2,8),lty=3,col='gray')
dev.off()

# Laboratory B - mixture system
A <- matrix(c(1,1,4,10),nrow=2,byrow=TRUE)
rhs <- c(20,140)
sol <- solve(A,rhs)
print(sol)
print(A %*% sol-rhs)
print(det(A))

# Laboratory C - secant slopes
h <- c(1,0.5,0.1,0.01,-0.01,-0.1)
slopes <- ((2+h)^2-4)/h
print(data.frame(h,slopes))
png('chapter03_secants_R.png')
plot(h,slopes,pch=19,xlab='h',ylab='Secant slope')
abline(h=4,lty=2,col='blue')
dev.off()
