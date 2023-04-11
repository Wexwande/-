import numpy as np
import matplotlib.pyplot as plt
freq = 1      
ampl = 1      
phase = 0     
t_start = 0  
t_end = 10    
dt = 0.01     
t = np.arange(t_start, t_end, dt)
oscillator = ampl * np.sin(2 * np.pi * freq * t + phase)
noise_amp = 0.2   
noise = noise_amp * np.random.randn(len(oscillator))
oscillator_noise = oscillator + noise
signal_power = np.sum(oscillator**2)/len(oscillator)
noise_power = np.sum(noise**2)/len(noise)
snr = 10*np.log10(signal_power/noise_power)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, oscillator)
ax1.set_title('Гармонический осцилятор')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.plot(t, oscillator_noise)
ax2.set_title('Гармонический осцилятор с шумом')
ax2.set_xlabel('Time')
ax2.set_ylabel('Amplitude')
plt.tight_layout()
plt.show()