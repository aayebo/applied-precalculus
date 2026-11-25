import numpy as np
import matplotlib.pyplot as plt
c = np.arange(6, dtype=float)
y = np.array([1.2,3.0,5.1,6.9,9.2,10.8])
b, a = np.polyfit(c,y,1)
pred = a+b*c
res = y-pred
rmse = np.sqrt(np.mean(res**2))
print(f"Intercept={a:.4f}; slope={b:.4f}; RMSE={rmse:.4f}")
fig, axes = plt.subplots(1,2,figsize=(9,3.5))
axes[0].scatter(c,y,label="Observations")
axes[0].plot(c,pred,label="Linear fit")
axes[0].set(xlabel="Concentration (mg/L)",ylabel="Signal (units)")
axes[0].legend()
axes[1].scatter(c,res)
axes[1].axhline(0,linestyle="--",color="gray")
axes[1].set(xlabel="Concentration (mg/L)",ylabel="Residual (units)")
fig.tight_layout()
fig.savefig("figures/labA_python.png",dpi=170)
plt.close(fig)
