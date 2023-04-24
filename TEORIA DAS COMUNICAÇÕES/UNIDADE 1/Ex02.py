import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Lê o sinal de áudio
rate, audio_signal = wav.read('true_love.wav')

# Exibe o sinal de aúdio original
plt.figure(figsize=(10, 5))
plt.title('Sinal de aúdio original')
plt.plot(audio_signal)
plt.xlabel('Índice de amostra')
plt.ylabel('Amplitude')
plt.show()

# Quantiza o sinal de áudio
# Usamos um nível de quantização de 8 bits
quantization_level = 2**8
audio_signal_quantized = (np.round(audio_signal / (2**15) * (quantization_level - 1)) / 
                         (quantization_level - 1) * (2**15)).astype(np.int16)

# Exibe sinal de aúdio quantizado
plt.figure(figsize=(10, 5))
plt.title('Sinal de áudio quantizado')
plt.plot(audio_signal_quantized)
plt.xlabel('Índice de amostra')
plt.ylabel('Amplitude')
plt.show()

# Calcula PSNR (Peak Signal-to-Noise Ratio)
# PSNR é a medida da qualidade do sinal quantizado
# Comparação com o sinal original
def psnr(original, quantized):
    mse = np.mean((original - quantized) ** 2)
    return 10 * np.log10(np.max(original)**2 / mse)

print("PSNR: {:.2f} dB".format(psnr(audio_signal, audio_signal_quantized)))

