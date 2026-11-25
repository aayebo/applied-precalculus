# Laboratory A: Sine and cosine transformations
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2*np.pi, 2*np.pi, 600)
f = 2*np.sin(3*(x-np.pi/6))+1
plt.figure()
plt.plot(x,f,label="Transformed sine")
plt.axhline(1,linestyle="--",label="Midline")
plt.xlabel("x (radians)"); plt.ylabel("f(x)")
plt.legend(); plt.tight_layout()
plt.savefig("chapter09_transformation_python.png"); plt.close()
print("Amplitude:",2,"Period:",2*np.pi/3,"Midline:",1)
key_x = np.pi/6 + np.arange(5)*(2*np.pi/3)/4
key_y = 2*np.sin(3*(key_x-np.pi/6))+1
for a,b in zip(key_x,key_y):
    print(f"x={a:.4f}, y={b:.4f}")
# Compare the exact period with measured peak separation
print("Period in radians:",2*np.pi/3)

# Laboratory B: tangent and reciprocal graphs
x = np.linspace(-2*np.pi,2*np.pi,3000)
cosx = np.cos(x)
tan_y = np.divide(np.sin(x),cosx)
sec_y = np.divide(1.0,cosx)
tan_y[np.abs(cosx)<0.035] = np.nan
sec_y[np.abs(cosx)<0.035] = np.nan
plt.figure()
plt.plot(x,tan_y,label="tangent")
plt.plot(x,sec_y,label="secant")
plt.ylim(-4,4); plt.xlabel("x (radians)"); plt.ylabel("y")
plt.legend(); plt.tight_layout()
plt.savefig("chapter09_reciprocal_python.png"); plt.close()
print("Tangent asymptotes: pi/2 + k*pi")
print("tan(pi/4):",np.tan(np.pi/4))
print("sec(pi/3):",1/np.cos(np.pi/3))

# Laboratory C: periodic model fitting
rng = np.random.default_rng(9)
t = np.arange(25)
observed = 37+0.4*np.cos(2*np.pi*(t-4)/24)+rng.normal(0,0.06,len(t))
X = np.column_stack([np.ones(len(t)),np.cos(2*np.pi*t/24),np.sin(2*np.pi*t/24)])
coef = np.linalg.lstsq(X,observed,rcond=None)[0]
pred = X @ coef
residual = observed-pred
print("Coefficients:",coef)
print("RMSE:",np.sqrt(np.mean(residual**2)))
plt.figure()
plt.scatter(t,observed,label="Observed")
plt.plot(t,pred,label="Fitted")
plt.xlabel("Time (hours)"); plt.ylabel("Temperature (C)")
plt.legend(); plt.tight_layout()
plt.savefig("chapter09_model_python.png"); plt.close()
