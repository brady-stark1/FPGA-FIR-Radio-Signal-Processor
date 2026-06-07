import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Parameters
sample_rate = 48000
cutoff_freq = 15000
num_taps = 32

# Design FIR filter
coeffs = firwin(
    num_taps,
    cutoff=cutoff_freq,
    fs=sample_rate
)

print("FIR Coefficients:")
print(coeffs)

# Frequency response
w, h = freqz(coeffs, worN=8000)

frequencies = w * sample_rate / (2 * np.pi)

plt.figure(figsize=(10,5))
plt.plot(frequencies, 20 * np.log10(np.abs(h)))

plt.title("FIR Filter Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.grid()
plt.show()

# Convert to floating point for Verilog

print("\nFixed-point coefficients:")

fixed_coeffs = np.round(coeffs * 32767).astype(int)

for c in fixed_coeffs:
    print(c)