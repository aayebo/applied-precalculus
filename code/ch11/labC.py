# Laboratory C: periodic regression and residuals
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(11)
t = np.arange(24, dtype=float); omega = 2*np.pi/24
y = 70 + 6*np.sin(omega*t) + 2*np.cos(omega*t) + 0.12*t
y = y + rng.normal(0, 0.5, len(t))
X = np.column_stack((np.ones(len(t)), np.sin(omega*t), np.cos(omega*t)))
D, B, C = np.linalg.lstsq(X, y, rcond=None)[0]
fitted = X @ np.array([D,B,C]); residuals = y-fitted
amp = np.hypot(B,C); phase = np.arctan2(C,B)
rmse = np.sqrt(np.mean(residuals**2))
print(f"Midline={D:.3f}, amplitude={amp:.3f}, "
      f"phase={phase:.3f} rad, RMSE={rmse:.3f}")
plt.figure(figsize=(8,4)); plt.scatter(t,y,label="Observed")
plt.plot(t,fitted,label="Fitted"); plt.xlabel("Time (hours)")
plt.ylabel("Sensor reading"); plt.legend(); plt.tight_layout()
plt.savefig("periodic_fit_python.png",dpi=160); plt.close()
plt.figure(figsize=(8,4)); plt.scatter(t,residuals)
plt.axhline(0,ls="--"); plt.xlabel("Time (hours)")
plt.ylabel("Residual"); plt.tight_layout()
plt.savefig("periodic_residuals_python.png",dpi=160); plt.close()
