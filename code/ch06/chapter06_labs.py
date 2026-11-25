# Chapter 6 computational laboratories - run from top to bottom
import numpy as np
import matplotlib.pyplot as plt

# LAB A: polynomial zeros and multiplicity
def P(x): return (x+1)*(x-2)**2
x = np.linspace(-3,4,600)
plt.figure(); plt.plot(x,P(x),label="(x+1)(x-2)^2")
plt.scatter([-1,2],[0,0]); plt.axhline(0,color="gray",linestyle="--")
plt.xlabel("x"); plt.ylabel("P(x)"); plt.grid(True); plt.legend(); plt.show()
print("Exact zeros:",[-1,2],"Values:",P(np.array([-1,2])))

# LAB B: rational function and vertical asymptote
def R(x): return (x+1)/(x-2)
left=np.linspace(-5,1.85,300); right=np.linspace(2.15,7,300)
plt.figure(); plt.plot(left,R(left),color="blue"); plt.plot(right,R(right),color="blue")
plt.axvline(2,color="red",linestyle="--",label="x=2")
plt.axhline(1,color="gray",linestyle="--",label="y=1")
plt.ylim(-12,12); plt.xlabel("x"); plt.ylabel("R(x)"); plt.legend(); plt.grid(True); plt.show()

# LAB C: saturation model
def S(c): return 100*c/(10+c)
c=np.linspace(0,100,300)
plt.figure(); plt.plot(c,S(c)); plt.axhline(100,color="red",linestyle="--")
plt.xlabel("Concentration (mg/L)"); plt.ylabel("Signal"); plt.grid(True); plt.show()
for value in [0,10,30,40]: print(value, S(value))
assert abs(S(40)-80)<1e-10
