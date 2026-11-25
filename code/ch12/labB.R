n <- 1:15
a <- 10; r <- 0.6
terms <- a*r^(n-1)
partial <- cumsum(terms)
formula <- a*(1-r^n)/(1-r)
print(data.frame(n, partial, formula, error=partial-formula))
plot(n, partial, type="b", pch=19, xlab="Number of terms", ylab="Partial sum", main="Convergent geometric series")
abline(h=a/(1-r), lty=2, col="red")
