# Applied investigation: Comparing two growth models
# 1. Define the input domain and model
x <- seq(0, 10, length.out = 301)
y <- 100*1.2^x-(100+20*x)

# 2. Inspect numerical predictions
idx <- unique(round(seq(1, length(x), length.out = 5)))
print(data.frame(input = x[idx], output = y[idx]))

# 3. Visualize the model with labeled axes
plot(x, y, type = "l", lwd = 2, col = "#176B87",
     xlab = "Time (h)", ylab = "Prediction difference")
grid()

# 4. Check the sampled output range
print(range(y))
