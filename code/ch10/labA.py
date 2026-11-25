# Laboratory A: identities and numerical precision
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi, 2*np.pi, 1001)
e1 = np.sin(x)**2 + np.cos(x)**2 - 1
e2 = np.sin(2*x) - 2*np.sin(x)*np.cos(x)
print("Max Pythagorean error:", np.max(np.abs(e1)))
print("Max double-angle error:", np.max(np.abs(e2)))
plt.plot(x, e1)
plt.axhline(0, linestyle="--", color="black")
plt.xlabel("Angle (radians)")
plt.ylabel("Numerical difference")
plt.title("Floating-point identity check")
plt.tight_layout()
plt.savefig("labA_python.png", dpi=160)
plt.close()
