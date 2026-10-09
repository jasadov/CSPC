"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 16

def k_imbalance(x):
    return (2*x)**2/((1 - x)*(1 - x)) - K

x_newton = newton(k_imbalance, 0.5)

res = minimize(lambda v: k_imbalance(v[0])**2, x0=[0.5],
               method="SLSQP", bounds=[(0, 0.99)])
x_slsqp = res.x[0]

print("Newton:", x_newton)
print("SLSQP:", x_slsqp)
print("H2 = I2 =", 1 - x_newton)
print("HI =", 2*x_newton)

xs = np.linspace(0, 0.99, 300)
plt.plot(xs, 1 - xs, label="H2")
plt.plot(xs, 1 - xs, "--", label="I2")
plt.plot(xs, 2*xs, label="HI")
plt.axvline(x_newton, color="k", linestyle=":", label="equilibrium")
plt.xlabel("x")
plt.ylabel("amount, mol")
plt.legend()
plt.savefig("equilibrium.png", dpi=150)