import math
import matplotlib.pyplot as plt
import numpy as np

temp_values = [200, 298, 400, 500]
omega_values = [15000, 10, 22500]

dictionary1 = {}
dictionary2 = {}

mole_fractions = ['Xa', 'Xb']
dictionary1['Xa'] = 506
dictionary1['Xb'] = 430

dictionary2['Xa'] = 'A'
dictionary2['Xb'] = 'B'

for mole_fraction in mole_fractions:
    for omega in omega_values:
        for temp in temp_values:
            x = []
            y = []

            for X in np.arange(0.1, 1.1, 0.1):
                U = dictionary1[mole_fraction] + 8.314 * temp * 2.303 * math.log(X) + omega * (1 - (X ** 2))
                x.append(X)
                y.append(U)
            plt.plot(x, y, label = str(temp) + 'K', marker = 'o')
            plt.xlabel(mole_fraction)
            plt.ylabel('Chemical Potential of ' + dictionary2[mole_fraction])
            plt.title('Chemical potential of ' + dictionary2[mole_fraction] + ' vs ' + mole_fraction + ' at omega = ' + str(omega))
            plt.legend()
        plt.show()