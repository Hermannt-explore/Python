#This script reads a .wav file

import sys
import numpy
import struct
import wave
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plot

def read_wave():
    filter_freq = int(sys.argv[1])
    frame_rate = 48000.0
    num_samples = 48000
    wave_file = wave.open("sample0.wav", 'r')
    data = wave_file.readframes(num_samples)
    wave_file.close()
    #unpack data from 16 bit short int
    data = struct.unpack( '{n}h'.format(n=num_samples), data)
    #convert data to array
    data = numpy.array(data)
    #convert data array to frequency domain
    data_freq = numpy.fft.fft(data)
    frequencies = numpy.abs(data_freq)
    #plot the wave data in time and frequency domain
    plot.subplot(2,2,1,1)
    plot.plot(data[:300])
    plot.title("Original signal time domain")
    plot.subplot(2,2,2,1)
    plot.plot(frequencies[:1200])
    plot.title("Original signal frequency domain")
    filtered_data_freq = []
    filtered_data_freq = [val if (filter_fred-10 < index < filter_freq+10 and val>1) else 0 for index, val enumerate(frequencies)]
    plotsubplot(2,2,2,2)
    plot.plot(filtered_data_freq[1200])
    plot.title("filtered signal frequency domain")
    plot.subplot(2,2,1,2)
    plot.plot(filtered_data_time[:300])
    plot.title("filtered signal time domain")
    plot.savefig('plot.png')

read_wave();

