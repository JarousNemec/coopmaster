import matplotlib.pyplot as plt
import numpy as np

# Konfigurace časové osy (4 hodiny, každá minuta je jeden bod)
minutes = np.arange(0, 241)

# Inicializace hmotnosti na 0 (prázdné hnízdo)
weights = np.zeros_like(minutes)

# Vstup první slepice (hmotnost kolem 2000 gramů) na 20. minutě
weights[20:48] = np.random.normal(loc=2000, scale=50, size=28)

# Po odchodu slepice zůstává jedno vejce (55 gramů)
weights[48:186] = np.random.normal(loc=55, scale=3, size=len(weights[48:186]))

# Vstup druhé slepice (hmotnost kolem 2000 gramů) na 186. minutě
weights[186:223] = np.random.normal(loc=2000, scale=50, size=37)

# Po odchodu slepice zůstávají dvě vejce (přibližně 115 gramů)
weights[223:241] = np.random.normal(loc=115, scale=5, size=len(weights[223:241]))

# Vizualizace časové řady
plt.figure(figsize=(12, 6))
plt.plot(minutes, weights, marker='o', linestyle='-')
plt.axhline(y=50, color='r', linestyle='--', label='50g - prázdné/práh')
plt.axhline(y=1200, color='g', linestyle='--', label='1200g - slepice/práh')

plt.title('Časová řada hmotnosti hnízda')
plt.xlabel('Čas (minuty)')
plt.ylabel('Hmotnost (gramy)')
plt.legend()
plt.grid(True)
plt.show()

