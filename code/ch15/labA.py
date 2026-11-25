import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
Path("figures").mkdir(exist_ok=True)
a = 2.0
f = lambda x: x*x + 3*x
h = np.array([1, .5, .1, .01, -.01, -.1, -.5])
print("h, secant slope, exact simplified slope")
for step in h:
    print(f"{step:8.3f} {(f(a+step)-f(a))/step:12.6f} {2*a+step+3:12.6f}")
x = np.linspace(-1, 4, 300)
plt.plot(x, f(x), label="f(x)=x^2+3x")
plt.plot(x, f(a)+7*(x-a), label="tangent estimate at a=2")
plt.scatter([a],[f(a)])
plt.xlabel("x");plt.ylabel("f(x)");plt.legend();plt.tight_layout()
plt.savefig("figures/labA_python.png", dpi=180)
plt.close()
