# Laboratory B: solving sin(x) = 1/2 numerically
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4*np.pi, 2001)
roots = np.array([np.pi/6, 5*np.pi/6, 13*np.pi/6, 17*np.pi/6])
print("Root and residual:")
for r in roots:
    print(f"{r:.9f}  {np.sin(r)-0.5:.2e}")
plt.plot(x, np.sin(x), label="sin(x)")
plt.axhline(0.5, color="red", linestyle="--", label="target")
plt.scatter(roots, np.sin(roots), color="black")
plt.xlabel("x (radians)")
plt.legend()
plt.tight_layout()
plt.savefig("labB_python.png", dpi=160)
plt.close()
