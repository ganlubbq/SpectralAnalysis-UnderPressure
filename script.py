#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Spectral analysis of Freddie Mercury's voice singing "Under Pressure"

Data is from the video available in YouTube where only the voices of Freddie 
Mercury and David Bowie were recorded.
(link: https://www.youtube.com/watch?v=uMQb9LCNGxs)

I focused the analysis to interval 1:53 to 2:10 of the song 

@author: plcr
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from scipy.io import wavfile
from scipy.signal import butter, welch, spectrogram, lfilter, get_window

#%% Take data from the original .wav file

# reading .wav file
filename = './under_pressure-original.wav'
fs,data = wavfile.read(filename)
data = data.astype(float)

# choosing interval of time we're interested (in seconds)
t_ini = 102
t_end = 131
interval = range(102*fs, 131*fs)

# taking just one of the channels from the stereo recording
s = data[interval,0]

# low pass filtering the audio signal until 4kHz
N  = 6 # order of the butterworh filter
fc = 4e3 # cut frequency
wc = fc*1.0/(fs/2.0) 
b,a = butter(N=6,Wn=wc)
y = lfilter(b,a,s)

# downsample the signal from 44100 Hz to 11025 Hz
yd = y[::4]
fsd = fs/4

# normalize the signal from -1 to +1
yn = 2*(yd-np.min(yd)) / (np.max(yd)-np.min(yd)) - 1

L = 1024
f,t,Sxx = spectrogram(yn, fs=fsd, window=get_window('hamming', L),
                      nperseg=L, noverlap=(1024-64))

Sxx = Sxx/np.mean(Sxx)

#%% plot the figure

I = 10*np.log10(Sxx)
fig,ax = plt.subplots(facecolor='white', figsize=(16,7))
ax.imshow(I, aspect='auto', origin='lower', extent=[t[0], t[-1], f[0], f[-1]])
ax.set_ylim(0, 4000)
ax.set_ylabel('frequency (Hz)', fontsize=16)
ax.set_xlabel('seconds (s)', fontsize=16)
tit = ax.set_title('Spectrogram using Hamming window with L = 1024 points (values in dB)', fontsize=20)
tit.set_position((0.5, 1.02))

plt.savefig('spectrogram.pdf', format='pdf')
plt.savefig('spectrogram.png', format='png')
plt.savefig('spectrogram.eps', format='eps')

#%%

I = 10*np.log10(Sxx)
fig = plt.figure(facecolor='white', figsize=(16,7))
gs = gridspec.GridSpec(2, 2, height_ratios=[4, 1], width_ratios=[80, 1], hspace=0.015) 

ax0 = plt.subplot(gs[0,0])
im = ax0.imshow(I, aspect='auto', origin='lower', extent=[t[0], t[-1], f[0], f[-1]])
ax0.set_ylim(0, 1000)
ax0.set_ylabel('frequency (Hz)', fontsize=16)
ax0.set_xticks([])
tit = ax0.set_title('Spectrogram using Hamming window with L = 1024 points (intensity in dB)', fontsize=20)
tit.set_position((0.5, 1.02))

time = np.linspace(0,t[-1],len(yn))
ax1 = plt.subplot(gs[1,0])
ax1.plot(time, yn, lw=0.8)
ax1.set_xlabel('seconds (s)', fontsize=16)
ax1.set_ylabel('normalized\namplitude', fontsize=16)
ax1.set_ylim(-1.4, +1.4)
ax1.set_xlim(time[0], time[-1])

ax2 = plt.subplot(gs[0,1])
clb = plt.colorbar(im, cax=ax2)
clb.set_ticks([-120, -90, -60, -30, 0, 30])
clb.set_ticklabels(['-120', '-90', '-60', '-30', '0', '30'])
clb.ax.set_position([0.84, 0.27, 0.01, 0.63])

plt.savefig('spectrogram_duo.png', format='png')
