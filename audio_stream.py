import pyaudio
import numpy as np
import parameters
from weighting_filter import weighting_filter
import matplotlib.pyplot as plt

class audio_stream(object):

    def __init__(self, format      = parameters.FORMAT,
                 channels          = parameters.CHANNELS,
                 rate              = parameters.sample_rate,
                 input             = True,
                 frames_per_buffer = parameters.CHUNK):
        
        self.stream             = pyaudio.PyAudio()
        self.format             = format
        self.channels           = channels
        self.rate               = rate
        self.input              = input
        self.frames_per_buffer  = frames_per_buffer
        self.test = "ieeei"

    def fft(self, data):
        
        print(max(data))
        N = int( parameters.sample_rate / 20000)
        data = data * np.hanning(len(data)) # smooth the FFT by windowing data
        fft = abs(np.fft.fft(data).real) / N
        fft = fft[:int(len(fft)/2)] # keep only first half
        freq = np.fft.fftfreq(parameters.CHUNK,1.0/parameters.sample_rate)
        freq = freq[:int(len(freq)/2)] # keep only first half
        print(max(fft))
        freqPeak = freq[np.where(fft==np.max(fft))[0][0]] + 1
        print("peak frequency: %d Hz"%freqPeak)
        return fft
    
    def audio_stream(self, filter_val=None):
        '''
        Starts audio streaming
        '''

        stream = self.stream.open(  format            = parameters.FORMAT,
                                    channels          = parameters.CHANNELS,
                                    rate              = parameters.sample_rate,
                                    input             = True,
                                    frames_per_buffer = parameters.CHUNK)

        data = np.fromstring(stream.read(parameters.CHUNK), dtype=np.int16)
        data = filter_val[0:len(data)]
        print(max(data))        
        fig, ax = plt.subplots()
        # if filter:
        #     fft_audio = self.fft(data)
        #     filtered_audio = fft_audio * filter_val[0:len(fft_audio)]
        plt.semilogx((data))
        # plt.semilogx(20 * np.log10(fft_audio)-40)
        plt.grid(which="both")
        plt.show()

if __name__ == '__main__':

    WF = weighting_filter()
    filter_val = WF.weighting_filter(weight='A')
    # print(len(filter_val[0:2]))
    audio_test = audio_stream()
    audio_test.audio_stream(filter_val)