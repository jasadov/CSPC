import time
from decay import simulate, simulate_loop

N0 = 200000
rate = 0.4

start = time.perf_counter()
simulate_loop(N0, rate)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, rate)
numpy_time = time.perf_counter() - start

print(f"Pure-Python loop: {loop_time:.4f} s")
print(f"NumPy vectorised: {numpy_time:.4f} s")
print(f"NumPy is {loop_time / numpy_time:.1f}x faster")