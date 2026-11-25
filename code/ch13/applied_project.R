# Applied investigation: Elliptical cross section
# 1. Define the input domain and model
x <- seq(-5, 5, length.out = 301)
y <- 3*sqrt(pmax(0,1-x^2/25))

# 2. Inspect numerical predictions
idx <- unique(round(seq(1, length(x), length.out = 5)))
print(data.frame(input = x[idx], output = y[idx]))

# 3. Visualize the model with labeled axes
plot(x, y, type = "l", lwd = 2, col = "#176B87",
     xlab = "Horizontal position (cm)", ylab = "Vertical position (cm)")
grid()

# 4. Check the sampled output range
print(range(y))
