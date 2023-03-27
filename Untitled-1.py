import numpy as np 
import matplotlib.pylab as plt
x = np.linspace(0, 100, 200)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()