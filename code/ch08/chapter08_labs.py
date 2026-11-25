# Chapter 8: Angles, radians, and the unit circle
import math
import numpy as np
import matplotlib.pyplot as plt

# Laboratory A: unit-circle coordinates
angles = np.array([0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi])
for angle in angles:
    x, y = math.cos(angle), math.sin(angle)
    print(f"theta={angle:.5f}, x={x:.5f}, y={y:.5f}, error={x*x+y*y-1:.2e}")
theta = np.linspace(0, 2*math.pi, 401)
plt.figure()
plt.plot(np.cos(theta), np.sin(theta))
plt.scatter(np.cos(angles), np.sin(angles))
plt.axis('equal'); plt.xlabel('cos(theta)'); plt.ylabel('sin(theta)')
plt.title('Unit circle'); plt.tight_layout(); plt.savefig('unit_circle_python.png'); plt.close()

# Laboratory B: arc length and sector area
for radius in [1, 2, 3]:
    for angle in [math.pi/6, math.pi/3, math.pi/2]:
        print(f"r={radius}, theta={angle:.4f}, arc={radius*abs(angle):.4f}, area={0.5*radius**2*abs(angle):.4f}")

# Laboratory C: circular motion
time = np.linspace(0, 4, 401)
radius, omega, phase = 2, math.pi/2, math.pi/4
x = radius*np.cos(omega*time + phase)
y = radius*np.sin(omega*time + phase)
plt.figure(); plt.plot(time, x); plt.xlabel('Time (s)'); plt.ylabel('x-coordinate')
plt.title('Horizontal coordinate'); plt.tight_layout(); plt.savefig('circular_coordinate_python.png'); plt.close()
plt.figure(); plt.plot(x,y); plt.axis('equal'); plt.xlabel('x'); plt.ylabel('y')
plt.title('Circular path'); plt.tight_layout(); plt.savefig('circular_path_python.png'); plt.close()
