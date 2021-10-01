
import numpy as np
from parameters import k, pressure_ref


def spl(rms):
    '''
    This function calculates the sound pressure level in dB.
    p_rms: root mean square pressure level
    pressure_ref: reference pressure level (20uPa at 1KHz)
    '''

    return 10 * np.log10((rms / pressure_ref)**2)

def rms(pressure_level):
    '''
    This funciotns calculates the root mean square
    of the given pressure by a specific period of time
    pressure_level: pressure level given by the microphone in Pa
    '''

    return np.sqrt((abs(pressure_level)**2.0).mean())

def frequency_weighting():
    '''
    
    '''

def pascal_in_db(pressure_ref):
    return 20 * log10(1 / pressure_ref)   

def calibrate_microphone(mic_recording, freq_sample, SPL_reading, freq_weighting, pressure_ref):
    '''
    This fuction returns the calibration factor of the microphone.
    To run this function, you must connect a microphone to your audio card, generate a 1 kHz tone using an external device, 
    and use an SPL meter to determine the true loudness level.
    The calibration must take, at least, 3 seconds

    ARGUMENTS INPUT
    mic_recording: This is the microphone recording passed 
    through the weighting filter specified in the FrequencyWeighting

    freq_sample: Sample rate of microphone recording (usually 44.1K Hz)

    SPL_reading: Sound pressure level reported from physical meter (dB)

    pressure_ref: 20e-6 (default)

    ARGUMENTS OUTPUT
    calibration_factor: Microphone calibration factor

    To determine the calibration factor for a microphone, the calibrateMicrophone function uses:

        1) A calibration tone recorded from the microphone you want to calibrate.

        2) The sample rate used by your sound card for AD conversion.

        3) The known loudness, usually determined using a physical SPL meter.

        4) The frequency weighting used by your physical SPL meter.

        5) The atmospheric pressure at the recording location.
    '''


    mic_recording = filter_weight(mic_recording, freq_weighting)

    calibration_factor = (10 ** (SPL_reading - k)) / rms(mic_recording)

    return calibration_factor



