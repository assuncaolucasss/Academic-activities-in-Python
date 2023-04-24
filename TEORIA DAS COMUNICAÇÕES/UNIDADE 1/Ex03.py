import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Lê o sinal de áudio
rate, audio_signal = wav.read('still_in_live.wav')

# Exibe o sinal de áudio original
plt.figure(figsize=(10, 5))
plt.title('Sinal de áudio original')
plt.plot(audio_signal)
plt.xlabel('Índice de amostra')
plt.ylabel('Amplitude')
plt.show()

# Adiciona ruído ao sinal
noise_power = 100  # Modifica a potência do ruído
noise = np.random.normal(0, noise_power, audio_signal.shape)
audio_signal_noisy = audio_signal + noise

# Exibe o sinal de aúdio ruidoso
plt.figure(figsize=(10, 5))
plt.title('Sinal de áudio ruidoso')
plt.plot(audio_signal_noisy)
plt.xlabel('Índice de amostra')
plt.ylabel('Amplitude')
plt.show()

# Calcula a relação sinal-ruído (SNR)
# SNR é uma medida da qualidade do sinal na presença de ruído
def snr(original, noisy):
    signal_power = np.mean(original**2)
    noise_power = np.mean((original - noisy)**2)
    return 10 * np.log10(signal_power / noise_power)

print("SNR: {:.2f} dB".format(snr(audio_signal, audio_signal_noisy)))

