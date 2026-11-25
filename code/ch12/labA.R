n <- 1:12
arithmetic <- 4 + 3*(n-1)
geometric <- 4 * 1.5^(n-1)
print(data.frame(n, arithmetic, geometric))
cat("First overtake:", n[which(geometric > arithmetic)[1]], "\n")
plot(n, arithmetic, pch=19, col="blue", ylim=range(c(arithmetic, geometric)), xlab="Term index", ylab="Term value", main="Arithmetic and geometric sequences")
points(n, geometric, pch=17, col="red")
legend("topleft", c("Arithmetic", "Geometric"), col=c("blue","red"), pch=c(19,17))
