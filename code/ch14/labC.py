# Laboratory C: component uncertainty, reproducible simulation
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(14)
n = 2000
x = rng.uniform(2.8,3.2,n); y = rng.uniform(3.8,4.2,n)
magnitude = np.hypot(x,y)
print('Nominal magnitude:',5)
print('Simulated min/max:',magnitude.min(),magnitude.max())
print('Componentwise theoretical bounds:',np.hypot(2.8,3.8),np.hypot(3.2,4.2))
fig, ax = plt.subplots()
ax.scatter(x,y,s=4,alpha=.35); ax.scatter([3],[4],s=55)
ax.set(xlabel='Horizontal displacement (m)',ylabel='Vertical displacement (m)',title='Component uncertainty')
ax.set_aspect('equal'); ax.grid(True); fig.savefig('figures/labC_python.png',dpi=180,bbox_inches='tight')
