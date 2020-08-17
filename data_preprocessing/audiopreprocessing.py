# -*- coding: utf-8 -*-

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile

file = "flute.mp4"

#waveform in time domain
signal_1D_np, sample_rate = librosa.load(file,sr=22050)

# no of items in the array = sampling rate(22020) * length of the audio in seconds

# librosa.display.waveplot(signal_1D_np, sr = sample_rate)
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.show()        

#in frequency domain
# fft_sound = np.fft.fft(signal_1D_np)
# magnitude = np.abs(fft_sound)
# frequency = np.linspace(0,sample_rate,len(magnitude))

# left_half_magnitude = magnitude[:int(len(magnitude)/2)]
# left_half_frequency = frequency[:int(len(frequency)/2)]

# plt.plot(left_half_frequency, left_half_magnitude)
# plt.xlabel("Frequency")
# plt.ylabel("Magnitude")
# plt.show()

#claculate stft and dsiplay spectogram
n_fft = 4088 
hop_length = 512

spectogram = librosa.stft(signal_1D_np, n_fft = n_fft, hop_length = hop_length)
mag = np.abs(spectogram)
phase = np.angle(spectogram)

wav = librosa.istft(spectogram, hop_length=hop_length)
audRate = 22050
wavfile.write('recon_flute.wav', audRate, wav)



#log_spectogram = librosa.amplitude_to_db(mag)
# librosa.display.specshow(log_spectogram,sr=sample_rate, hop_length=hop_length)
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.colorbar()
# plt.show()

#MFCC
# MFCCs = librosa.feature.mfcc(signal_1D_np, n_fft = n_fft, hop_length = hop_length, n_mfcc=13)
# librosa.display.specshow(MFCCs,sr=sample_rate, hop_length=hop_length)
# plt.xlabel("Time")
# plt.ylabel("Frequency")
# plt.colorbar()
# plt.show()
