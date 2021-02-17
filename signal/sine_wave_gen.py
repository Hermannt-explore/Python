#This script creates a sine wave and writes it to a file

import numpy
import wave
import struct
import matplotlib.pyplot as plot


def wave_create():

    #freq = 1KHz sampling_rate = 48Khz
    freq = 1000
    noise_freq = 500
    num_samples = 48000

    #ADC variables
    samp_rate = 48000.0
    amplitude = 16000


    #creating sine wave values
    mywave = [numpy.sin(2 * numpy.pi * freq * x/samp_rate) for x in range (num_samples)]
    noise_wave = [numpy.sin(2 * numpy.pi * noise_freq * x/samp_rate) for x in range (num_samples)]
    mywave = numpy.array(mywave)
    noise_wave = numpy.array(noise_wave)
    final_wave = mywave + noise_wave
    
    #writting parameters
    nframes = num_samples
    comptype = "NONE"
    compname = "not compressed"
    nchannels = 1
    sampwidth = 2

    #setting up file for writting
    wav_file = wave.open ("sample0.wav", 'w')
    wav_file.setparams((nchannels, sampwidth, int(samp_rate), nframes, comptype, compname))

    #writting sine wave values to file
    for val in final_wave:
        wav_file.writeframes(struct.pack('h', int(val*amplitude)))
    wav_file.close()
wave_create()
