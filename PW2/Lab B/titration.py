"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.

import numpy as np
import matplotlib.pyplot as plt

V, pH = np.loadtxt("titration.csv", delimiter=",", skiprows=1, unpack=True)
slope = np.gradient(pH, V)
V_eq = V[np.argmax(slope)]
print("Equivalence point:", V_eq, "mL")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(V, pH)
ax[0].axvline(V_eq, linestyle=":")
ax[0].set_title("pH curve")
ax[1].plot(V, slope)
ax[1].axvline(V_eq, linestyle=":")
ax[1].set_title("slope dpH/dV")
for a in ax:
    a.set_xlabel("V, mL")
plt.savefig("titration.png", dpi=150)