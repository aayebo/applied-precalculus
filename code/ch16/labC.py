import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0,49,3,dtype=float)
y = 70+8*np.sin(2*np.pi*(t-3)/24)+0.7*np.cos(0.8*t)
plt.figure(figsize=(7,4))
plt.scatter(t,y,label="Synthetic observations")
for period in [22,24,26]:
    dense = np.linspace(0,48,400)
    model = 70+8*np.sin(2*np.pi*(dense-3)/period)
    plt.plot(dense,model,label=f"Period {period} h")
res = y-(70+8*np.sin(2*np.pi*(t-3)/24))
print(f"Nominal-period RMSE={np.sqrt(np.mean(res**2)):.4f}")
plt.xlabel("Time (hours)")
plt.ylabel("Signal (units)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/labC_python.png",dpi=170)
plt.close()
