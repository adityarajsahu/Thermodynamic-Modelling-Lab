import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

NbRe_database = Database(r'TDB Files\Nb_Re.TDB')
comps = ["NB", "RE"]
NbRe_phases = ['CHI_RENB', 'SIGMARENB', 'FCC_RENB', 'LIQUID_RENB', 'BCC_RENB', 'HCP_RENB']
conditions = {
    v.P: 101325,
    v.T: (1000, 3500, 20),
    v.X('RE'): (0, 1, 0.01)
}

fig, ax = plt.subplots()
binplot(NbRe_database, comps, NbRe_phases, conditions)
plt.show()