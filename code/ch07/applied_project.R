# Applied investigation: Decay of a fluorescent signal
# 1. Define the input domain and model
x <- seq(0, 12, length.out = 301)
y <- 80*0.75^x

# 2. Inspect numerical predictions
idx <- unique(round(seq(1, length(x), length.out = 5)))
print(data.frame(input = x[idx], output = y[idx]))

# 3. Visualize the model with labeled axes
plot(x, y, type = "l", lwd = 2, col = "#176B87",
     xlab = "Time (h)", ylab = "Intensity")
grid()

# 4. Check the sampled output range
print(range(y))
