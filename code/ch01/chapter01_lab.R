# Chapter 1 — Applied Precalculus Using R and Python
# Lab A: arithmetic and numeric representation (base R only)
print((-3)^2)
print(-3^2)
print((2.4e6) * 0.015)
print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3)
print(isTRUE(all.equal(0.1 + 0.2, 0.3)))
# Rational expression: original domain excludes x=0 and x=3
x <- c(-2, 1, 4)
original <- (x^2 - 9) / (x^2 - 3*x)
simplified <- (x + 3) / x
print(data.frame(x, original, simplified))
# Lab B: tolerance graph
x <- seq(-1, 7, length.out=501)
plot(x, abs(x-3), type='l', lwd=2, col='navy',
     xlab='x', ylab='Distance from 3', main='Absolute value and tolerance')
abline(h=2, col='firebrick', lty=2, lwd=2)
abline(v=c(1,5), col='gray60', lty=3)
print(data.frame(x=c(1,3,5), distance=abs(c(1,3,5)-3)))
# Lab C: dimensional analysis and simple linear model
mass_g <- 0.075
print(paste('Mass in mg:', mass_g*1000))
v <- seq(0,10,length.out=101)
plot(v, 0.4*v, type='l', lwd=2, col='navy',
     xlab='Volume (mL)', ylab='Mass (mg)',
     main='Illustrative laboratory mass model')
