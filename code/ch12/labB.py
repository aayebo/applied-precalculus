import numpy as np
import matplotlib.pyplot as plt
n = np.arange(1, 16)
a, r = 10.0, 0.6
terms = a*r**(n-1)
partial = np.cumsum(terms)
formula = a*(1-r**n)/(1-r)
print("Largest discrepancy:", np.max(np.abs(partial-formula)))
for k, s in zip(n, partial): print(f"S_{k} = {s:.6f}")
plt.plot(n, partial, "o-"); plt.axhline(a/(1-r), linestyle="--", label="Infinite sum")
plt.xlabel("Number of terms"); plt.ylabel("Partial sum"); plt.legend(); plt.tight_layout()
plt.savefig("labB_python.png", dpi=180); plt.close()
