import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

AlNi_database = Database(r'TDB Files\NI_AL_DUPIN_2001.TDB')
comps = ["AL", "NI", "VA"]
AlNi_phases = AlNi_database.phases.keys()
conditions = {
    v.N: 1, 
    v.P: 101325,
    v.T: (300, 2000, 10),
    v.X('AL'): (1e-5, 1, 0.02)
}

fig, ax = plt.subplots()
binplot(AlNi_database, comps, AlNi_phases, conditions)
plt.show()