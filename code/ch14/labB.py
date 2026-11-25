# Laboratory B: polar curves
import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0, 2*np.pi, 1500)
fig, axes = plt.subplots(1,2,figsize=(10,4))
for ax, r, title in [(axes[0],2*np.cos(3*theta),'Three-petal rose'),(axes[1],1+2*np.cos(theta),'Limacon with inner loop')]:
    ax.plot(r*np.cos(theta),r*np.sin(theta))
    ax.set_aspect('equal'); ax.set_title(title); ax.set_xlabel('x'); ax.set_ylabel('y'); ax.grid(True)
fig.tight_layout(); fig.savefig('figures/labB_python.png',dpi=180,bbox_inches='tight')
