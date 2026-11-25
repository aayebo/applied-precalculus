# Applied investigation: Repeated sampling accumulation
# 1. Define the input domain and model
x <- 1:15
y <- 500*(1-0.8^x)

# 2. Inspect numerical predictions
idx <- unique(round(seq(1, length(x), length.out = 5)))
print(data.frame(input = x[idx], output = y[idx]))

# 3. Visualize the model with labeled axes
plot(x, y, type = "p", lwd = 2, col = "#176B87",
     xlab = "Completed rounds", ylab = "Cumulative units")
grid()

# 4. Check the sampled output range
print(range(y))
