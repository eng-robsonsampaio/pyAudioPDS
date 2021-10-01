import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

class Wave:

    def __init__(self, freq_sample, period, time_sampling, chunk):
        '''
        freq_sample: frequency sample
        period: sample period
        ts: time sampling
        
        '''
        self.freq_sample = freq_sample
        self.period = period
        self.time_sampling = time_sampling
        self.chunk = chunk

    def create_sin_wave(self, magnitude, freq, t_vec):
        omega = 2*np.pi*freq
        return magnitude*np.sin(omega*t_vec)

    
if __name__=="__main__":

    freq_sample = 44100
    period = 1/freq_sample
    time_sampling = 0.1
    chunk = freq_sample*time_sampling
    
    # create a wave object
    wave = Wave(freq_sample, period, time_sampling, chunk)
    t_vec = np.arange(wave.chunk)*wave.period

    sin = wave.create_sin_wave(magnitude=1, freq=40, t_vec=t_vec)
    plt.plot(t_vec,sin)
    plt.show()
    