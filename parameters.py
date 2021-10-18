import numpy as np
import pyaudio

# Width of analysis bands, specified as 'Full band', '1 octave', '2/3 octave', or '1/3 octave'.
band_width = 'full band'

# Frequency range of the filter bank in Hz, specified as a two-element row vector of positive monotonically increasing values. 
# Frequency bands centered above SampleRate/2 are excluded.
frequency_rage = (20, 20000)

# Order of the octave filter, specified as an even integer.
octave_filter_order = 2

# Frequency weighting applied to input, specified as 'A-weighting', 'C-weighting', or 'Z-weighting', 
# where Z-weighting corresponds to no weighting.
frequency_weighting =  'A-weighting'

# Time weighting, in seconds, for calculation of time-weighted sound level and maximum time-weighted sound level, specified as 'Fast' or 'Slow'.
# The TimeWeighting property is used to specify the coefficient of a lowpass filter.
# fast: 1/8, slow 1
time_weighting = 'fast' 

# Reference pressure for dB calculations in Pa, specified as a positive scalar.
pressure_reference = 2e-5

# Time interval, in seconds, to report equivalent-continuous, peak, and maximum time-weighted sound levels, specified as a positive scalar integer.
time_interval = 1

# Scalar (mono input) or vector (multichannel input) calibration factor multiplied by input.
# Use Calibrate class to set the calibration
calibration_factor = None

# Input sample rate in Hz, specified as a positive scalar.
sample_rate = 44100

# pascal relative to the PressureReference
k = 20 * np.log10(1 / pressure_reference)

## Audio characteristics 
# size of the audio streamed by 
CHUNK = 1024 * 2

# format of the data read
FORMAT = pyaudio.paInt16

# Quantity of channels | 1 : audio mono
CHANNELS = 1