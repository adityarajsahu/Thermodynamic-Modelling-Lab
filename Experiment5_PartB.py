from pycalphad import Database, equilibrium, variables as v
import numpy as np
import matplotlib.pyplot as plt

dbf = Database(r'TDB Files\alzn_mey.tdb')
exp_x_zn =   [0.0482, 0.1990, 0.3550, 0.5045, 0.6549, 0.8070, 0.9569]
exp_acr_zn = [0.1154, 0.3765, 0.5411, 0.6433, 0.7352, 0.8384, 0.9531]

comps = ['AL', 'ZN', 'VA']
phases = list(dbf.phases.keys())
ref_eq = equilibrium(dbf, comps, phases, {v.P: 101325, v.T: 1023, v.X('ZN'): 1})
eq = equilibrium(dbf, comps, phases, {v.P: 1013325, v.T: 1023, v.X('ZN'): (0, 1,
0.005)})
chempot_ref = ref_eq.MU.sel(component='ZN').squeeze()
chempot = eq.MU.sel(component='ZN').squeeze()
acr_zn = np.exp((chempot - chempot_ref)/(8.315*1023))

fig, ax = plt.subplots()

ax.plot(eq.X.sel(component='ZN', vertex=0).squeeze(), acr_zn, label='Calculated')
ax.scatter(exp_x_zn, exp_acr_zn, label='Yazawa 1970')
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.set_xlabel('X(ZN)')
ax.set_ylabel('ACR(ZN)')
ax.set_title('Activity of Zn at 1073K')
ax.legend()
plt.show()