# Chapter 4: Function tables and graphs
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-3,3.01,.5)
linear=2*x+1; quadratic=x**2-2*x
for a,b,c in zip(x,linear,quadratic): print(a,b,c)
plt.plot(x,quadratic,label='Quadratic'); plt.plot(x,linear,label='Linear')
plt.legend(); plt.grid(True); plt.savefig('chapter04_families.png'); plt.close()
x=np.linspace(-4,8,500); y=np.full_like(x,np.nan)
valid=(x>=2)&(np.abs(x-5)>1e-8)
y[valid]=np.sqrt(x[valid]-2)/(x[valid]-5)
plt.plot(x,y); plt.axvline(5,linestyle='--'); plt.ylim(-4,4)
plt.savefig('chapter04_domain.png'); plt.close()
for h in [1,.5,.1,.01,.001]: print(h,((2+h)**2-4)/h)
