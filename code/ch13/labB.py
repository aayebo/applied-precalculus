import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,400);x=3*np.cos(t);y=2*np.sin(t)
fig,ax=plt.subplots();ax.plot(x,y);ax.scatter([x[0]],[y[0]],label="start")
for k in [0,100,200,300]:ax.annotate("",xy=(x[k+5],y[k+5]),xytext=(x[k],y[k]),arrowprops={"arrowstyle":"->"})
ax.set_aspect("equal");ax.grid(True);ax.legend();ax.set_xlabel("x");ax.set_ylabel("y")
fig.savefig("labB_python.png",dpi=180);plt.close(fig)
