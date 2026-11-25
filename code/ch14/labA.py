# Laboratory A: vectors and projections
import math
import numpy as np
import matplotlib.pyplot as plt
u = np.array([4., 3.]); v = np.array([2., 1.])
dot = float(np.dot(u, v))
angle = math.degrees(math.acos(dot/(np.linalg.norm(u)*np.linalg.norm(v))))
projection = dot/np.dot(v,v)*v
residual = u-projection
print('Angle (degrees):', angle, 'Projection:', projection, 'Residual:', residual)
print('Residual dot v:', np.dot(residual,v))
fig, ax = plt.subplots()
for vec, color, name in [(u,'blue','u'),(v,'red','v'),(projection,'green','projection')]:
    ax.arrow(0,0,*vec,head_width=.13,length_includes_head=True,color=color,label=name)
ax.set(xlim=(0,5),ylim=(0,4),xlabel='x',ylabel='y',title='Vectors and projection')
ax.set_aspect('equal'); ax.grid(True); ax.legend(); fig.savefig('figures/labA_python.png',dpi=180,bbox_inches='tight')
