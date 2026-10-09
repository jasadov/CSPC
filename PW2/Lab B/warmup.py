"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

import numpy as np
from scipy.optimize import newton, minimize

f      = lambda x: (x-3)**2 + 1
fprime = lambda x: 2*(x-3)
fsec   = lambda x: 2.0

x, lr = 0.0, 0.1
for _ in range(200):
    x = x - lr*fprime(x)     
print("GD:", x)

print("Newton:", newton(fprime, 0.0, fprime=fsec))

res = minimize(lambda v: f(v[0]), x0=[0.0], method="SLSQP")
print("SLSQP:", res.x[0])

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

g = lambda x: x**4 - 3*x**2 + x + 5
gprime = lambda x: 4*x**3 - 6*x + 1
gsec = lambda x: 12*x**2 - 6

def run(x0):
    print("start x0 =", x0)

    x = x0
    for _ in range(1000):
        x = x - 0.01*gprime(x)
    print("Gradient descent:", x)

    xn = newton(gprime, x0, fprime=gsec)
    kind = "minimum" if gsec(xn) > 0 else "maximum"
    print("Newton:", xn, "g'' =", gsec(xn), "->", kind)

    res = minimize(lambda v: g(v[0]), x0=[x0], method="SLSQP")
    print("SLSQP:", res.x[0])

run(0)
run(2)
