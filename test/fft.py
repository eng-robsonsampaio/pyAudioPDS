import pyaudio
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)
N = int( RATE / 20000) # number of samples
p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(
            format=pyaudio.paInt16, #
            channels=1,rate=RATE, #
            input=True, #
            frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
# for i in range(10): #to it a few times just to see
data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
print(max(data))
data = data * np.hanning(len(data)) # smooth the FFT by windowing data
fft = abs(np.fft.fft(data).real) / N
# ref = 2*10**-5
# fft = 20 * np.log10(fft / ref)
fft = fft[:int(len(fft)/2)] # keep only first half
freq = np.fft.fftfreq(CHUNK,1.0/RATE)
freq = freq[:int(len(freq)/2)] # keep only first half
print(max(fft))
freqPeak = freq[np.where(fft==np.max(fft))[0][0]] + 1
print("peak frequency: %d Hz"%freqPeak)

# uncomment this if you want to see what the freq vs FFT looks like
plt.plot(freq,fft)
plt.axis([10,4010, 0 ,10*10**6])
plt.show()
plt.close()

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()

# import numpy as np
# import matplotlib.pyplot as plt
# import pyaudio

# # construct a time signal
# fs = 44100 # frequency sample
# tstep = 1/fs # sample time interval
# signal_frequency = 20000 #Hz (max signal frequency?)

# N = int(100* fs / signal_frequency) # number of samples

# t = np.linspace(0, (N-1)*tstep, N) # time steps
# fstep = fs / N
# f = np.linspace(0, (N-1)*fstep, N)

# signal = 1 * np.sin(2 * np.pi * signal_frequency * t) + 4 * np.sin(5 * np.pi * signal_frequency * t)

# # Perform FFT
# X = np.fft.fft(signal)
# X_mag = np.abs(X) / N

# f_plot = f[0:int(N / 2 + 1)]
# X_mag_plot = 2 * X_mag[0:int(N / 2 + +1)]
# X_mag_plot[0] = X_mag_plot[0] / 2 # DC component does not need to multiply by 2



# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
# ax1.plot(t, signal, '.-')
# ax2.plot(f_plot, X_mag_plot, '.-')
# plt.show()