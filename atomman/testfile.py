import iprPy
import atomman as am
import atomman.unitconvert as uc

calc = iprPy.load_calculation('diatom_scan')
print(calc.maindoc)
print(calc.theorydoc)

print(calc.calc.__doc__)

#potential_name = '1999--Mishin-Y--Ni--LAMMPS--ipr1'
potential_name = '2011--Zhou-X-W--Li-Na-K-Rb-Cs-F-Cl-Br-I--LAMMPS--ipr1'

# Retrieve potential and parameter file(s) using atomman
potential = am.load_lammps_potential(id=potential_name, getfiles=True,status=None)

result = calc.calc(
    lammps_command='lmp',
    potential=potential,
    symbols='Cl',
    rmin=uc.set_in_units(0.02, 'angstrom'),
    rmax=uc.set_in_units(6, 'angstrom'),
    rsteps=300
)

r = uc.get_in_units(result['r_values'], 'angstrom')
E = uc.get_in_units(result['energy_values'], 'eV')

print(result)

import matplotlib.pyplot as plt

plt.plot(r, E)
plt.xlabel('Distance (Å)')
plt.ylabel('Energy (eV)')
plt.xlim(2,6)
plt.ylim(-.3,.4)
plt.title('Diatom Scan')
plt.grid(True)
plt.show()

