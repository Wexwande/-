import numpy as np
import matplotlib.pyplot as plt
amplitude = 1
omega = 1
t = np.arange(0, 10, 0.01)
y = amplitude * np.sin(omega * t)
plt.plot(t, y)
plt.title('Harmonic oscillator')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
noise_amplitude = 0.5
y_noise = y + noise_amplitude * np.random.normal(size=t.size)
plt.plot(t, y_noise, label='noise')
plt.plot(t, y, label='harmonic oscillator')
plt.title('Harmonic oscillator with noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
signal_power = np.mean(y)
noise_power = np.mean(noise_amplitude)
SNR = signal_power / noise_power
print('SNR =', SNR)