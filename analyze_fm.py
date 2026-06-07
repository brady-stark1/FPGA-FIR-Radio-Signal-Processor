import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load WAV
sample_rate, data = wavfile.read("fm_recording.wav")

print("Sample rate:", sample_rate)
print("Shape:", data.shape)
print("Dtype:", data.dtype)

# If stereo, take one channel
if len(data.shape) == 2:
    data = data[:, 0]

# Convert to float
data = data.astype(np.float32)
data = data / np.max(np.abs(data))

# Plot waveform
plt.figure(figsize=(12, 4))
plt.plot(data[:5000])
plt.title("FM Recording - Waveform")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

# FFT
n = len(data)
fft_vals = np.fft.rfft(data)
fft_freqs = np.fft.rfftfreq(n, d=1 / sample_rate)
fft_mag = np.abs(fft_vals)

plt.figure(figsize=(12, 5))
plt.plot(fft_freqs, fft_mag)
plt.title("FM Recording - Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, sample_rate / 2)
plt.tight_layout()
plt.show()