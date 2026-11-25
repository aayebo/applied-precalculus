# Laboratory C: periodic sensor and threshold times
import numpy as np
import matplotlib.pyplot as plt
def sensor(t):
    return 2 + 0.8*np.sin(np.pi*t/3)
t = np.linspace(0, 12, 1201)
crossings = np.array([0.5, 2.5, 6.5, 8.5])
for time in crossings:
    print(f"t={time:.1f} s, sensor={sensor(time):.3f}")
plt.plot(t, sensor(t), label="sensor")
plt.axhline(2.4, color="red", linestyle="--", label="threshold")
plt.scatter(crossings, sensor(crossings), color="black")
plt.xlabel("Time (seconds)")
plt.ylabel("Sensor units")
plt.legend()
plt.tight_layout()
plt.savefig("labC_python.png", dpi=160)
plt.close()
