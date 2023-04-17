import numpy as np
import matplotlib.pyplot as plt
u0, v0, m = 1.0, 0.0, 1.0
omega = np.sqrt(1 / 1) 
gamma = 0.2 * np.sqrt(1 / 1)
ravnoves = 8
np_array = np.linspace(ravnoves, 50, 500)
plt.plot(np.insert(np.linspace(ravnoves, 50, 500), 0, np.linspace(1, ravnoves, ravnoves//1)), np.insert(np.exp(-gamma / (2 * m) * np_array) * (u0 * np.cos(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * np_array) + (v0 + gamma / (2 * m) * u0) * np.sin(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * np_array)), 0, [0] * ravnoves))
plt.plot([ravnoves, ravnoves], [-1, 1], 'r--')
plt.xlabel('Время, с')
plt.ylabel('Смещение, м')
plt.show()