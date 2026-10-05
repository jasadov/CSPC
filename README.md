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