import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,400);u=np.linspace(-1.4,1.4,300)
fig,ax=plt.subplots(1,2,figsize=(10,4))
ax[0].plot(3*np.cos(t),2*np.sin(t));ax[0].set_title("Ellipse")
ax[1].plot(2*np.cosh(u),3*np.sinh(u));ax[1].plot(-2*np.cosh(u),3*np.sinh(u))
x=np.linspace(-5,5,200);ax[1].plot(x,1.5*x,"--");ax[1].plot(x,-1.5*x,"--")
ax[1].set_title("Hyperbola")
for a in ax:a.set_aspect("equal",adjustable="box");a.grid(True);a.set_xlabel("x");a.set_ylabel("y")
fig.tight_layout();fig.savefig("labA_python.png",dpi=180);plt.close(fig)
