"""Chapter 3 computational laboratories: run each section in order."""
import numpy as np
import matplotlib.pyplot as plt

# Laboratory A: calibration line
concentration = np.array([2., 8.])
signal = np.array([9., 27.])
m = (signal[1]-signal[0])/(concentration[1]-concentration[0])
b = signal[0]-m*concentration[0]
print('Laboratory A: slope, intercept, predicted signal:', m, b, m*5+b)
x = np.linspace(0,12,200)
plt.figure(); plt.scatter(concentration, signal, color='black')
plt.plot(x,m*x+b)
plt.axvline(2,ls='--',color='gray'); plt.axvline(8,ls='--',color='gray')
plt.xlabel('Concentration (mg/L)');plt.ylabel('Signal (units)');plt.tight_layout();plt.savefig('chapter03_calibration.png');plt.close()

# Laboratory B: mixture system
A=np.array([[1.,1.],[4.,10.]])
rhs=np.array([20.,140.])
sol=np.linalg.solve(A,rhs)
print('Laboratory B: volumes:',sol,'residual:',A@sol-rhs,'det:',np.linalg.det(A))

# Laboratory C: secant slopes
h=np.array([1.,0.5,0.1,0.01,-0.01,-0.1])
slopes=((2+h)**2-4)/h
print('Laboratory C: h and secant slopes:',list(zip(h,slopes)))
plt.figure();plt.scatter(h,slopes);plt.axhline(4,ls='--',color='black')
plt.xlabel('h');plt.ylabel('Secant slope');plt.tight_layout();plt.savefig('chapter03_secants.png');plt.close()
