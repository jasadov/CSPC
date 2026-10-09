"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

t, C = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1, unpack=True)
C0 = C[0]

def total_error(k):
    k = np.ravel(k)[0]
    return np.sum((C - C0*np.exp(-k*t))**2)

res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print("k =", k_fit)

tt = np.linspace(t.min(), t.max(), 200)
plt.plot(t, C, "o", label="data")
plt.plot(tt, C0*np.exp(-k_fit*tt), label=f"fit k={k_fit:.3f}")
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.savefig("kinetics.png", dpi=150)