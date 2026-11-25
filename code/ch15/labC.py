import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
Path("figures").mkdir(exist_ok=True)
rng = np.random.default_rng(15)
def C(t): return 10*np.exp(-.25*t)
t = np.linspace(0,8,81)
noise = rng.normal(0,.04,len(t))
y = C(t)+noise
dt = t[1]-t[0]
rate = np.diff(y)/dt
truth = -.25*C(t[:-1])
print("time, observed forward rate, model instantaneous rate")
for i in range(0,len(rate),10): print(round(t[i],2),round(rate[i],4),round(truth[i],4))
plt.plot(t[:-1],rate,label="noisy forward differences")
plt.plot(t[:-1],truth,label="model instantaneous rate")
plt.xlabel("time (hours)");plt.ylabel("rate (mg/L/hour)")
plt.legend();plt.tight_layout();plt.savefig("figures/labC_python.png",dpi=180)
plt.close()
