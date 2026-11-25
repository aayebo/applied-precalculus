# Chapter 5: Applied Precalculus — sequential Python laboratories

# LAB A: TRANSFORMATIONS
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4, 6, 500)
f = lambda z: z**2
plt.plot(x, f(x), label="x^2")
plt.plot(x, -2*f(x-2)+5, label="-2(x-2)^2+5")
plt.ylim(-4, 12)
plt.xlabel("x"); plt.ylabel("Output")
plt.legend(); plt.grid(True); plt.show()

# LAB B: COMPOSITION AND DOMAINS
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2, 2, 401)
g = lambda z: 3-z**2
f = lambda u: np.sqrt(u)
y = np.full_like(x, np.nan)
valid = g(x) >= 0
y[valid] = f(g(x[valid]))
plt.plot(x, y)
plt.xlabel("x"); plt.ylabel("f(g(x))")
plt.grid(True); plt.show()
print("Domain:", -np.sqrt(3), np.sqrt(3))

# LAB C: INVERSE CALIBRATION
import numpy as np
import matplotlib.pyplot as plt
signal = lambda c: 0.8*c+2
inverse = lambda s: (s-2)/0.8
c = np.linspace(0, 20, 101)
plt.plot(c, signal(c))
plt.xlabel("Concentration (mg/L)")
plt.ylabel("Signal (mV)"); plt.grid(True); plt.show()
for s in [2, 6, 10, 18]:
    print(f"Signal {s:.1f} -> concentration {inverse(s):.2f}")
assert np.allclose(inverse(signal(c)), c)
