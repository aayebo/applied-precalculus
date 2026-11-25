import numpy as np
import matplotlib.pyplot as plt
n = np.arange(1, 13)
arithmetic = 4 + 3*(n-1)
geometric = 4 * 1.5**(n-1)
for k, x, y in zip(n, arithmetic, geometric):
    print(f"n={k:2d} arithmetic={x:7.2f} geometric={y:9.2f}")
print("First overtake:", n[np.where(geometric > arithmetic)[0][0]])
plt.plot(n, arithmetic, "o", label="Arithmetic")
plt.plot(n, geometric, "^", label="Geometric")
plt.xlabel("Term index"); plt.ylabel("Term value"); plt.legend(); plt.tight_layout()
plt.savefig("labA_python.png", dpi=180); plt.close()
