#! /usr/bin/python

import sys
import pyaudio
from struct import unpack, calcsize
import numpy as np
from scipy.fftpack import fft, fftfreq, rfft
import matplotlib.pyplot as plt
import time
import equations as eq

#%matplotlib tk

CHUNK = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CALIBRATION_FACTOR = 1

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, (ax, ax2) = plt.subplots(2)

x = np.arange(0, 2 * CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)
line_fft, = ax2.plot(x_fft, np.random.rand(CHUNK), '-', lw=2)

ax.set_title('Audio Waveform')
ax.set_xlabel('samples')
ax.set_ylabel('magnitude')
ax.set_ylim(-32768 , 32767 )
ax.set_xlim(0, CHUNK)

ax2.set_xlim(0, RATE)
ax2.set_ylim(0, 10**6)


# plt.show(block=False)

# while True:

buffer = stream.read(CHUNK, exception_on_overflow=False)

audio = np.frombuffer(buffer, dtype=np.int16)    

# adicionar um fator de calibração:
audio =  audio * CALIBRATION_FACTOR

# Frequência de ponderação para cálculo do NPS Global
freq_ponderation = 0

# Valor da pressão sonora de referência para o cálculo do NPS
pressure_ref = 2e-5

# Cálculo do NPS Global
global_nps = 10 * np.log10(eq.rms(audio)**2 / pressure_ref**2) - freq_ponderation

line.set_ydata(audio)
audio_fft = rfft(audio)


line_fft.set_ydata(audio_fft)
# line_fft.set_ydata(np.abs(y_audio_fft))


# fig.canvas.draw()
# fig.canvas.flush_events()

# p_ref = 2**-5
# p_rms = eq.p_rms(audio)
# spl_dB = eq.SPL(p_rms, p_ref)
# spl_dB = 20 * np.log10(abs(np.mean(audio)) / 1)
print(global_nps)

plt.show()