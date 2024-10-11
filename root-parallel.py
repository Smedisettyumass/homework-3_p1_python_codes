import numpy as np
from scipy.optimize import fsolve
from joblib import  Parallel, delayed

import time

def f(x):
    return np.sin(3*np.pi*np.cos(2*np.pi*x) * np.sin(np.pi*x))


def find_root(guess):
    return fsolve(f, guess)[0]

a = -1
b = 3
n = 5**8
x0 = np.linspace(a, b, n)

start_time = time.time()

q =  Parallel(n_jobs=-1)(delayed(find_root)(x) for x in x0)


end_time = time.time()

q = np.unique(q)

print(f"Unique roots found: {q}")
print(f"Time taken: {end_time - start_time} seconds")
