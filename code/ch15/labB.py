import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
Path("figures").mkdir(exist_ok=True)
def g(x):
    return np.where(x < 2, x+1, 5-x)
for h in [.1,.01,.001]:
    print(f"h={h:g}, left={g(2-h):.6f}, right={g(2+h):.6f}")
x = np.linspace(0,4,401)
plt.plot(x,g(x),label="continuous piecewise model")
plt.scatter([2],[3]);plt.xlabel("x");plt.ylabel("g(x)")
plt.legend();plt.tight_layout();plt.savefig("figures/labB_python.png",dpi=180)
plt.close()
