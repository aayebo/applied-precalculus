import numpy as np
import matplotlib.pyplot as plt
n = np.arange(1, 26)
b = 12.0
for r in (0.7, 0.85):
    x = np.zeros(len(n)); x[0] = 12
    for k in range(1, len(n)): x[k] = r*x[k-1]+b
    equilibrium = b/(1-r)
    explicit = equilibrium+(x[0]-equilibrium)*r**(n-1)
    assert np.allclose(x, explicit)
    print(f"r={r}, equilibrium={equilibrium:.2f}, first six={np.round(x[:6],2)}")
    plt.plot(n, x, "o-", label=f"r={r}")
    plt.axhline(equilibrium, linestyle="--", alpha=0.5)
plt.xlabel("Measurement index"); plt.ylabel("Modeled amount (mg)"); plt.legend(); plt.tight_layout()
plt.savefig("labC_python.png", dpi=180); plt.close()
