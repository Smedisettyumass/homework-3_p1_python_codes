import numpy as np
from scipy.optimize import fsolve
import time

def f(x):
    return np.sin(3*np.pi*np.cos(2*np.pi*x)*np.sin(np.pi*x))


a = -1
b = 3
n = 5**8
x0 = np.linspace(a,b,n)
q =  np.zeros(len(x0))


start_time = time.time()
for i in range(n):
    q[i] = fsolve(f, x0[i])[0] 

end_time = time.time()

q =  np.unique(q)

print(f"Unique roots found: {q}")
print("time taken: ", end_time - start_time, " seconds")
