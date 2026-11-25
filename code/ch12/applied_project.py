# Applied investigation: Repeated sampling accumulation
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the input domain and model
x = np.arange(1, 16)
y = 500*(1-0.8**x)

# 2. Inspect numerical predictions
idx = np.unique(np.linspace(0, len(x)-1, 5).round().astype(int))
print(np.column_stack((x[idx], y[idx])))

# 3. Visualize the model with labeled axes
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.plot(x, y, "o", color="#176B87", linewidth=2)
ax.set(xlabel="Completed rounds", ylabel="Cumulative units")
ax.grid(alpha=0.22)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
plt.show()

# 4. Check the sampled output range
print(np.min(y), np.max(y))
