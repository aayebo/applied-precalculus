"""Chapter 1 parallel Python laboratory. Requires matplotlib."""
import math
import matplotlib.pyplot as plt
# Lab A
print('(-3)^2:', (-3)**2)
print('-(3^2):', -(3**2))
print('Scientific notation:', (2.4e6)*0.015)
print('0.1 + 0.2:', 0.1+0.2)
print('Exact equality:', 0.1+0.2 == 0.3)
print('Approximate equality:', math.isclose(0.1+0.2,0.3))
for x in [-2,1,4]:
    original=(x*x-9)/(x*x-3*x)
    simplified=(x+3)/x
    print('x, original, simplified:', x, original, simplified)
# Lab B
xs=[-1+8*i/500 for i in range(501)]
plt.figure()
plt.plot(xs,[abs(x-3) for x in xs],label='|x - 3|')
plt.axhline(2,color='firebrick',linestyle='--',label='Tolerance 2')
for boundary in (1,5): plt.axvline(boundary,color='gray',linestyle=':')
plt.xlabel('x'); plt.ylabel('Distance from 3'); plt.legend(); plt.tight_layout()
plt.savefig('chapter01_tolerance_python.png',dpi=180); plt.close()
print('Boundary checks:', [(x,abs(x-3)) for x in (1,3,5)])
# Lab C
print('Mass in mg:',0.075*1000)
v=[10*i/100 for i in range(101)]
plt.figure(); plt.plot(v,[0.4*z for z in v]); plt.xlabel('Volume (mL)')
plt.ylabel('Mass (mg)'); plt.title('Illustrative laboratory mass model')
plt.tight_layout(); plt.savefig('chapter01_mass_model_python.png',dpi=180); plt.close()
