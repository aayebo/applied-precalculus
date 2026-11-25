# Laboratory A: the ambiguous SSA case
import math
A = math.radians(30); a = 7; b = 10
s = b * math.sin(A) / a
if abs(s) > 1:
    print("No triangle")
else:
    for B in (math.asin(s), math.pi - math.asin(s)):
        C = math.pi - A - B
        if C > 0:
            c_side = a * math.sin(C) / math.sin(A)
            print(f"B={math.degrees(B):.2f} deg, "
                  f"C={math.degrees(C):.2f} deg, c={c_side:.3f}")
