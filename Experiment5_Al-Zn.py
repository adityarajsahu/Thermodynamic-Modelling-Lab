import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

AlZn_database = Database(r'TDB Files\Al-Zn.tdb')
AlZn_phases = ["LIQUID", "FCC_A1", "HCP_A3"]
fig, ax = plt.subplots()
binplot(AlZn_database, ["AL", "ZN", "VA"], AlZn_phases, {v.X("ZN"): (0, 1, 0.02), v.T: (300, 1000, 10), v.P: 101325, v.N: 1})
plt.show()