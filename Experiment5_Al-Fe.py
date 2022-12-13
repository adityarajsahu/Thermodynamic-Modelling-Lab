import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

AlFe_database = Database(r'TDB Files\alfe_sei.TDB')
comps = ["AL", "FE", "VA"]
AlFe_phases = ['LIQUID', 'B2_BCC', 'FCC_A1', 'HCP_A3', 'AL5FE2', 'AL2FE', 'AL13FE4', 'AL5FE4']
conditions = {
    v.N: 1, 
    v.P: 101325,
    v.T: (300, 2000, 10),
    v.X('AL'): (1e-5, 1, 0.02)
}

fig, ax = plt.subplots()
binplot(AlFe_database, comps, AlFe_phases, conditions)
plt.show()