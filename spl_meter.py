import parameters


class spl_meter(object):
    '''
    Criates a SPL object that performs SPL metering

    '''

    def __init__(self, band_width   = parameters.band_width, 
                frequency_range     = parameters.frequency_range,
                octave_filter_order = parameters.octave_filter_order,
                frequency_weighting = parameters.frequency_weighting,
                time_weighting      = parameters.time_weighting,
                pressure_reference  = parameters.pressure_refence,
                time_interval       = parameters.time_interval,
                calibration_factor  = parameters.calibrition_factor, 
                sample_rate         = parameters.sample_rate):

        
        