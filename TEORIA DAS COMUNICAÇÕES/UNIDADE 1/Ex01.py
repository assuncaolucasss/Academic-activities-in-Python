import numpy as np
import matplotlib.pyplot as plt

#Onda quadrada como valores de 0 a 1 alternando em intervalos de 10 unidades
sqrWave = np.concatenate((np.ones(10), np.zeros(10), np.ones(10), np.zeros(10), np.ones(10), np.zeros(10), np.ones(10), np.zeros(10)))

nP = 0.001  #potência do ruído
corruptType = 0  # 0: ruído
                 # 1: atenuação
                 # 2: distorção

#estrutura condicional para aplicação da modificação do sinal original
if corruptType == 0:  #geração de um sinal aleatório somado com o sinal original
  a = sqrWave + np.sqrt(nP)*np.random.randn(len(sqrWave))
elif corruptType == 1:  #atenuação do sinal pela metade
  a = 1*sqrWave
else: #distorção do sinal através da convolução com a resposta ao impulso do sistema
  a = np.convolve(sqrWave, 0.4*np.array([0.2, 0.3, 0.5, 0.4, 0.35, 0.31, 0.27]))

plt.plot(sqrWave, linewidth=3)  #plot do sinal original
plt.plot(a, 'g--', linewidth=3)  #plot do sinal modificado
plt.show()
