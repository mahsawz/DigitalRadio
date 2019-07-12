import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from playsound import playsound
import os
import time

print("Reading Signals. Please wait...")
data = np.loadtxt("input.txt")
print("Reading Finished")
amplify_factor = 2
cnt = 0

while True:

    w0 = int(input("Please select a frequency (96k,144k,288k,240k) : \n"))
    print("Processing...")
    N = 480000  # sampling rate
    cosine_values = 0.5 * (np.exp(np.array([1j * i * w0 * 2 * np.pi / N for i in range(len(data))])) + np.exp(
        np.array([-1j * i * w0 * 2 * np.pi / N for i in range(len(data))])))
    frequency = np.multiply(data, cosine_values)
    frequency = np.fft.fft(frequency)
    frequency *= amplify_factor

    for i in range(30000, len(frequency) - 30000):
        frequency[i] = 0

    frequency = np.fft.ifft(frequency)
    file_name = 'mt' + str(cnt) + '.wav'
    wav.write(file_name, N, frequency.astype(np.dtype('i2')))
    print("Done. Playing...")
    playsound(file_name)  # play
    cnt += 1
    f = None
