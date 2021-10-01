import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft

from tkinter import TclError

## Audio characteristics 

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 


fig, (ax, ax2) = plt.subplots(2, figsize=(15, 8))

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)


# variavle for plotting
x = np.arange(0, 2 * CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)


# data = stream.read(CHUNK)
# data_int16 = struct.unpack(str(CHUNK) + 'h', data)

# create a line object with random data
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)
line_fft, = ax2.plot(x_fft, np.random.rand(CHUNK), '-', lw=2)

print(type(line))
print(type(line_fft))

# Basic formatting for the axes
ax.set_title('Audio Waveform')
ax.set_xlabel('Samples')
ax.set_ylabel('Volume')
ax.set_ylim(0,255)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[-512, 0, 511])

ax2.set_xlim(20, RATE / 2)

print('Stream started')
# show the plot
plt.show(block=False)

frame_out = 0
start_time = time.time()

while True:

    data = stream.read(CHUNK)

    data_np = np.frombuffer(data, dtype=np.int16)
    # data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # data_np = np.array(data_int, dtype='b')[::2] + 128

    line.set_ydata(data_np)

    # y_fft = fft(data_int)
    # line_fft.set_ydata(data_np)
    # line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) * 2 / (256 * CHUNK))

    #
    ref = 1
    dbF = 20 * np.log10(abs(np.mean(data_np)) / ref)
    print(dbF)

    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_out += 1
    
    except TclError:

        frame_rate = frame_out / (time.time() - start_time)

        print('Stream stopped')
        print('Average frame rate = {:0f} FPS'.format(frame_rate))
        break