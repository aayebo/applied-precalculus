# Applied investigation: Water tank monitoring
# 1. Define the input domain and model
x <- seq(0, 20, length.out = 301)
y <- pmin(20+4*x,60)

# 2. Inspect numerical predictions
idx <- unique(round(seq(1, length(x), length.out = 5)))
print(data.frame(input = x[idx], output = y[idx]))

# 3. Visualize the model with labeled axes
plot(x, y, type = "l", lwd = 2, col = "#176B87",
     xlab = "Time (min)", ylab = "Volume (L)")
grid()

# 4. Check the sampled output range
print(range(y))
