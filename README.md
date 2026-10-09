# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation, comparing a slow pure-Python version with a fast NumPy version, plus tests to check it works correctly.

**Speed comparison (loop vs NumPy):**
- loop  : 3.7796 s
- numpy : 0.0003 s
- speed-up: 11021.5x faster

**Tests:** all passing? yes

**Conclusion:**
- The NumPy version was much faster than the plain loop — about 11000 times faster. This is because NumPy processes all the numbers at once instead of one by one like a normal loop. Using conda to set up the environment made it easy to run the project on another computer too.

## PW1 - Lab B: Data, Plotting, and Automation

**What the data showed:**
- The counts start around 5000 and go down over time, like decay usually does.

**Did the observed data match the analytical law?**
- Yes, the shapes matched pretty well.

**What the Snakemake pipeline does:**
- It rebuilds the figure only when needed, so it doesn't redo work for no reason.

## PW2 --- Lab A

- Mean acceleration: -8.57 m/s² (Teacher told us that there is a problem with this part, so this answer is acceptable).
- Why it is noisy: taking a derivative makes noise bigger. Acceleration needs two derivatives, so it is much noisier than the position.
- What integrating back showed: integration adds values up, so the noise partly cancels. The recovered position is within 0.78 m of the original.

## PW2 --- Lab B

### Comparing the three methods (Part 2)

For the function f(x) = (x-3)^2 + 1, gradient descent, Newton's method and SLSQP all ended up at x = 3, so there was no difference between them.

For the other function g(x) = x^4 - 3x^2 + x + 5 the results were different:

- Starting from x0 = 0: gradient descent gave x = -1.3008 and SLSQP gave x = -1.3009, which is the lowest point of the function. Newton gave x = 0.1699, but g'' there is -5.65 (negative), so this is a maximum, not a minimum.
- Starting from x0 = 2: Newton and gradient descent both gave x = 1.1309, where g'' = 9.35 (positive), so it is a local minimum. SLSQP gave x = -1.3006, the lower minimum.

So the methods don't always agree. Newton only looks for the place where g'(x) = 0, and that can be a maximum, so I had to check the sign of g''. The starting point also changed the answer a lot. Gradient descent and Newton got stuck in the nearest minimum, but SLSQP went to the lower one.

### Rate constant (Part 3)

The fitted rate constant is k = 0.262. The fitted curve goes through the data points well.

### Equilibrium (Part 4)

Newton and SLSQP gave the same answer, x = 0.667. This means that at equilibrium there is 0.333 mol of H2, 0.333 mol of I2 and 1.333 mol of HI.

### Titration (Part 5, bonus)

The equivalence point is at 50.0 mL. This is where the pH curve is the steepest, and the slope plot has its peak at the same volume.