import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

AlMg_database = Database(r'TDB Files\Al-Mg_Zhong.tdb')
comps = ["AL", "MG", "VA"]
AlMg_phases = AlMg_database.phases.keys()
fig, ax = plt.subplots()
binplot(AlMg_database, comps, AlMg_phases, {v.X("MG"): (0, 1, 0.02), v.T: (300, 1000, 10), v.P: 101325, v.N: 1})
plt.show()