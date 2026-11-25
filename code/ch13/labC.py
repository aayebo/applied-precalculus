import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng(13);t=np.linspace(0,2*np.pi,80);a,b=4,2
r=1+rng.normal(0,0.04,len(t));x=a*r*np.cos(t);y=b*r*np.sin(t)
residual=np.sqrt((x/a)**2+(y/b)**2)-1
fig,ax=plt.subplots(1,2,figsize=(10,4));ax[0].scatter(x,y,s=12)
u=np.linspace(0,2*np.pi,300);ax[0].plot(a*np.cos(u),b*np.sin(u));ax[0].set_aspect("equal")
ax[1].scatter(t,residual,s=12);ax[1].axhline(0,linestyle="--")
ax[0].set_title("Simulated observations");ax[1].set_title("Normalized radial residuals")
fig.tight_layout();fig.savefig("labC_python.png",dpi=180);plt.close(fig)
print("Mean residual:",np.mean(residual),"SD:",np.std(residual))
