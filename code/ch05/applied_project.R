# Applied investigation: Temperature sensor conversion
# 1. Define the input domain and model
x <- seq(0.5, 3, length.out = 301)
y <- 20*(x-0.5)

# 2. Inspect numerical predictions
idx <- unique(round(seq(1, length(x), length.out = 5)))
print(data.frame(input = x[idx], output = y[idx]))

# 3. Visualize the model with labeled axes
plot(x, y, type = "l", lwd = 2, col = "#176B87",
     xlab = "Voltage (V)", ylab = "Temperature (C)")
grid()

# 4. Check the sampled output range
print(range(y))
