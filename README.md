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