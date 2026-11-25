# Laboratory A
import numpy as np
import matplotlib.pyplot as plt
a, b, c0 = 3, -4, -2
D = b**2 - 4*a*c0
roots = np.array([(-b - np.sqrt(D))/(2*a),
                  (-b + np.sqrt(D))/(2*a)])
def f(x):
    return a*x**2 + b*x + c0
for root in roots:
    print(f"root={root:.6f}, residual={f(root):.2e}")
x = np.linspace(-1.5, 3, 400)
plt.plot(x, f(x), linewidth=2)
plt.axhline(0, color="black", linestyle="--")
plt.scatter(roots, f(roots))
plt.xlabel("x"); plt.ylabel("3x^2 - 4x - 2")
plt.tight_layout(); plt.show()

# Laboratory B
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 8, 401)
g = (t - 2)*(t - 6)
mask = g <= 0
plt.plot(t, g, linewidth=2)
plt.axhline(0, color="black", linestyle="--")
plt.scatter(t[mask], g[mask], s=5)
for boundary in (2, 6):
    plt.axvline(boundary, linestyle=":")
print("grid approximation:", t[mask].min(), t[mask].max())
plt.xlabel("Time (hours)")
plt.ylabel("(t - 2)(t - 6)")
plt.tight_layout(); plt.show()

# Laboratory C
def f(x):
    return x**3 - x - 1
left, right = 1.0, 2.0
assert f(left)*f(right) < 0
for k in range(25):
    mid = (left + right)/2
    if f(left)*f(mid) <= 0:
        right = mid
    else:
        left = mid
root = (left + right)/2
print("root =", root, "residual =", f(root),
      "width =", right-left)
