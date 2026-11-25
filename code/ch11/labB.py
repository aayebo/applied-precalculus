# Laboratory B: navigation and triangulation
import math
legs = [(12, 60), (8, 150)]
east = sum(d*math.sin(math.radians(az)) for d,az in legs)
north = sum(d*math.cos(math.radians(az)) for d,az in legs)
distance = math.hypot(east, north)
azimuth = math.degrees(math.atan2(east, north)) % 360
print(f"East={east:.3f}, North={north:.3f} km")
print(f"Distance={distance:.3f} km, azimuth={azimuth:.2f} deg")
A, B = map(math.radians, (48, 67))
T = math.pi-A-B; baseline = 100
print(f"AT={baseline*math.sin(B)/math.sin(T):.3f} m, "
      f"BT={baseline*math.sin(A)/math.sin(T):.3f} m")
