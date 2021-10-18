
import numpy as np
from scipy.signal.filter_design import bilinear
import matplotlib.pyplot as plt

class weighting_filter():

    def __init__(self, method='test', sample_rate=44100):
        self.method = method
        self.sample_rate = sample_rate
        self.f = np.arange(20, 20000, np.pi)

    def weighting_filter(self, weight='A'):

        f1 = 20.598997
        f2 = 107.65265
        f3 = 737.86223
        f4 = 12194.217
        Ra = ((12200 ** 2) * (self.f ** 4)) / (( (self.f ** 2) + 20.6**2) * ((self.f ** 2) + 12200 **2 ) * np.sqrt(((self.f ** 2) + 107.7**2 ) * ( (self.f ** 2) + 737.9**2 )))
        Rb = ((12200 ** 2) * (self.f ** 3)) / (( (self.f ** 2) + 20.6**2) * ((self.f ** 2) + 12200 **2 ) * np.sqrt(((self.f ** 2) + 158.5**2 )))
        Rc = ((12200 ** 2) * (self.f ** 2)) / (( (self.f ** 2) + 20.6**2) * ((self.f ** 2) + 12200 **2 ))

        

        fig, ax = plt.subplots()
        plt.semilogx(self.f, 2 + 20 * np.log10(Ra), label='A-Weighting')     
        plt.semilogx(self.f, 0.17 + 20 * np.log10(Rb), label='B-Weighting')  
        plt.semilogx(self.f, 0.06 + 20 * np.log10(Rc), label='C-Weighting')  
        plt.legend()   
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Magnitude [dB]')
        plt.title('Frequency Weighting')
        plt.grid(which="both")
        plt.show() 

        _filter = {'A' : Ra, 'B': Rb, 'C' : Rc}
        return _filter[weight]

    def weighting_filter_2():
    # %Sampling Rate
    # Fs = 48000;

    # Analog A-weighting filter according to IEC/CD 1672.
        f1 = 20.598997 
        f2 = 107.65265
        f3 = 737.86223
        f4 = 12194.217
        A1000 = 1.9997
        numerators =  [(2*np.pi*f4)**2 * (10**(A1000 / 20.0)), 0., 0., 0., 0.]
        denominators = np.convolve(
            [1., +4*pi * f4, (2*pi * f4)**2],
            [1., +4*pi * f1, (2*pi * f1)**2]
            ) 
        denominators = np.convolve(
                np.convolve(denominators,[1., 2 * np.pi * f3]), [1., 2 * np.pi * f2])

        # Bilinear transformation of analog design to get the digital filter. 
        (b,a) = np.bilinear(numerators,DEN,Fs)
        return (b, a)

if __name__ == '__main__':
    pass
    WF = weighting_filter()
    print(WF.weighting_filter(weight='A'))