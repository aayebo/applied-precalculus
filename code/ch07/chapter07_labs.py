# LAB A: Linear and exponential change
import math
import matplotlib.pyplot as plt
period = list(range(11))
linear = [100 + 20 * t for t in period]
exponential = [100 * 1.2**t for t in period]
for t, l, e in zip(period, linear, exponential):
    print(f"t={t:2d}: linear={l:.2f}, exponential={e:.2f}")
plt.figure()
plt.plot(period, exponential, "o-", label="Exponential")
plt.plot(period, linear, "s-", label="Linear")
plt.xlabel("Period")
plt.ylabel("Amount")
plt.title("Change models")
plt.legend()
plt.savefig("chapter07_models.png", dpi=180)
plt.close()
# End laboratory A

# LAB B: Half-life and inverse calculation
C0 = 32
k = 0.18
target = 5
half_life = math.log(2) / k
time_to_target = math.log(C0 / target) / k
check = C0 * math.exp(-k * time_to_target)
print("Half-life:", round(half_life, 4))
print("Time to target:", round(time_to_target, 4))
print("Verified concentration:", round(check, 4))
# End laboratory B

# LAB C: Log-linear fitting and residual inspection
import numpy as np
time = np.array([0, 2, 4, 6, 8], dtype=float)
measured = np.array([40, 26, 17, 10.8, 7.4], dtype=float)
rate, intercept = np.polyfit(time, np.log(measured), 1)
predicted = np.exp(intercept + rate * time)
residual = measured - predicted
for t, observed, fitted, error in zip(time, measured, predicted, residual):
    print(f"{t:.0f}: observed={observed:.2f}, predicted={fitted:.2f}, residual={error:.2f}")
print("Estimated A0:", round(math.exp(intercept), 4), "rate:", round(rate, 4))
plt.figure()
plt.plot(time, measured, "o", label="Observed")
plt.plot(time, predicted, "-", label="Fitted")
plt.xlabel("Time (hours)")
plt.ylabel("Concentration (mg/L)")
plt.legend()
plt.savefig("chapter07_fit.png", dpi=180)
plt.close()
plt.figure()
plt.plot(time, residual, "o")
plt.axhline(0, linestyle="--")
plt.xlabel("Time (hours)")
plt.ylabel("Observed - predicted")
plt.savefig("chapter07_residuals.png", dpi=180)
plt.close()
# End laboratory C
