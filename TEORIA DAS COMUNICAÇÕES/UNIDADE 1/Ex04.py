import numpy as np

# Suponha que o valor da potência recebida do receptor wifi esteja em miliwattsreceived_power_mW = 0.1  
# Converte a potência recebida de miliwatts para dBm

received_power_dBm = 10 * np.log10(received_power_mW)

print("Potência recebida: {:.2f} dBm".format(received_power_dBm))

