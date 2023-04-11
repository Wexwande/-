import numpy as np
import matplotlib.pyplot as plt
k = 1    
m = 1     
g = 9.81   
x0 = 0      
v0 = 0     
t_start = 0   
t_end = 30    
dt = 0.01     
t = np.arange(t_start, t_end, dt)
def spring_force(x):
    return -k * x
def gravity_force(x):
    return -m * g
def solve(x0, v0, t):
    x = np.zeros(len(t))    
    v = np.zeros(len(t))   
    x[0] = x0               
    v[0] = v0              
    for i in range(1, len(t)):
        x[i] = x[i-1] + v[i-1] * dt                                    
        f = spring_force(x[i]) + gravity_force(x[i])    
        a = f / m                                   
        v[i] = v[i-1] + a * dt                     
    return x, v
x1, v1 = solve(x0, v0, t)
x2, v2 = solve(x1[-1], v1[-1], t)
x3, v3 = solve(x2[-1] + 0.1, 0, t)
plt.plot(t, x1, label='До нарушения')
plt.plot(t, x2, label='После нарушения')
plt.plot(t, x3, label='В момент нарушения')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()