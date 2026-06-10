# Standard library imports
from pathlib import Path
import datetime
from math import floor
from typing import Optional

# http://www.numpy.org/
import numpy as np

# https://ipython.org/
from IPython.display import display, Markdown

# https://github.com/usnistgov/atomman
import atomman as am
import atomman.lammps as lmp
import atomman.unitconvert as uc
from atomman.tools import filltemplate, aslist
# Show atomman version
print('atomman version =', am.__version__)

# https://github.com/usnistgov/iprPy
import iprPy
from iprPy.tools import read_calc_file


import bokeh
print('Bokeh version =', bokeh.__version__)
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.resources import Resources
from bokeh.io import output_notebook

# Load the calculation being demoed
calculation = iprPy.load_calculation('diatom_scan')

# Display main docs and theory
#display(Markdown(calculation.maindoc))
#display(Markdown(calculation.theorydoc))


def diatom_scan(lammps_command: str,
                potential: am.lammps.Potential,
                symbols: list,
                mpi_command: Optional[str] = None,
                rmin: float = uc.set_in_units(0.02, 'angstrom'),
                rmax: float = uc.set_in_units(6.0, 'angstrom'),
                rsteps: int = 300) -> dict:
    """
    Performs a diatom energy scan over a range of interatomic spaces, r.

    Parameters
    ----------
    lammps_command :str
        Command for running LAMMPS.
    potential : atomman.lammps.Potential
        The LAMMPS implemented potential to use.
    symbols : list
        The potential symbols associated with the two atoms in the diatom.
    mpi_command : str, optional
        The MPI command for running LAMMPS in parallel.  If not given, LAMMPS
        will run serially.
    rmin : float, optional
        The minimum r spacing to use (default value is 0.02 angstroms).
    rmax : float, optional
        The maximum r spacing to use (default value is 6.0 angstroms).
    rsteps : int, optional
        The number of r spacing steps to evaluate (default value is 300).

    Returns
    -------
    dict
        Dictionary of results consisting of keys:

        - **'r_values'** (*numpy.array of float*) - All interatomic spacings,
          r, explored.
        - **'energy_values'** (*numpy.array of float*) - The computed potential
          energies for each r value.
    """

    # Build lists of values
    r_values = np.linspace(rmin, rmax, rsteps)
    energy_values = np.empty(rsteps)

    # Define atype based on symbols
    symbols = aslist(symbols)
    if len(symbols) == 1:
        atype = [1, 1]
    elif len(symbols) == 2:
        atype = [1, 2]
    else:
        raise ValueError('symbols must have one or two values')

    # Initialize system (will shift second atom's position later...)
    box = am.Box.cubic(a = rmax + 1)
    atoms = am.Atoms(atype=atype, pos=[[0.1, 0.1, 0.1], [0.1, 0.1, 0.1]])
    system = am.System(atoms=atoms, box=box, pbc=[False, False, False], symbols=symbols)

    # Add charges if required
    if potential.atom_style == 'charge':
        system.atoms.prop_atype('charge', potential.charges(system.symbols))

    # Get lammps units
    lammps_units = lmp.style.unit(potential.units)

    # Define lammps variables
    lammps_variables = {}

    # Loop over values
    for i in range(rsteps):

        # Shift second atom's x position
        system.atoms.pos[1] = np.array([0.1 + r_values[i], 0.1, 0.1])

        # Save configuration
        system_info = system.dump('atom_data', f='diatom.dat',
                                  potential=potential)
        lammps_variables['atomman_system_pair_info'] = system_info

        # Write lammps input script
        lammps_script = 'run0.in'
        template = read_calc_file('iprPy.calculation.diatom_scan', 'run0.template')
        with open(lammps_script, 'w') as f:
            f.write(filltemplate(template, lammps_variables, '<', '>'))

        # Run lammps and extract data
        try:
            output = lmp.run(lammps_command, script_name=lammps_script,
                             mpi_command=mpi_command)
        except:
            energy_values[i] = np.nan
        else:
            energy = output.simulations[0]['thermo'].PotEng.values[-1]
            energy_values[i] = uc.set_in_units(energy, lammps_units['energy'])

    if len(energy_values[np.isfinite(energy_values)]) == 0:
        raise ValueError('All LAMMPS runs failed. Potential likely invalid or incompatible.')

    # Collect results
    results_dict = {}
    results_dict['r_values'] = r_values
    results_dict['energy_values'] = energy_values

    return results_dict

# with open('run0.template', 'w') as f:
#     f.write("""#LAMMPS input script that evaluates a system's energy without relaxing
#
# <atomman_system_pair_info>
#
# thermo_style custom step pe
# thermo_modify format float %.13e
#
# run 0""")



lammps_command = 'lmp'
mpi_command = None

# Optional: check that LAMMPS works and show its version
#print(f'LAMMPS version = {am.lammps.checkversion(lammps_command)["version"]}')

#potential_name = '1999--Mishin-Y--Ni--LAMMPS--ipr1'
potential_name = '2011--Zhou-X-W--Li-Na-K-Rb-Cs-F-Cl-Br-I--LAMMPS--ipr1'

# Retrieve potential and parameter file(s) using atomman
potential = am.load_lammps_potential(id=potential_name, getfiles=True,status=None)

symbols = 'Cl'
rmin = uc.set_in_units(0.02, 'angstrom')
rmax = uc.set_in_units(6.0, 'angstrom')
rsteps = 300


results_dict = diatom_scan(lammps_command, potential, symbols,
                           mpi_command = mpi_command,
                           rmin = rmin,
                           rmax = rmax,
                           rsteps = rsteps)
print(results_dict.keys())
print(results_dict)
#
# for key,value in results_dict.items():
#     print(f"{key}: {value}")



length_unit = 'angstrom'
energy_unit = 'eV'

energy = uc.get_in_units(results_dict['energy_values'], energy_unit)
r = uc.get_in_units(results_dict['r_values'], length_unit)

Emin = floor(energy.min())
if Emin < -10:
    Emin = -10

plot = figure(title = f'Diatom energy scan for {potential_name}',
              width = 800,
              height = 600,
              x_range = [uc.get_in_units(rmin, 'angstrom'), uc.get_in_units(rmax, 'angstrom')],
              y_range = [Emin, 0],
              x_axis_label=f'r ({length_unit})',
              y_axis_label=f'Cohesive Energy ({energy_unit}/atom)')

plot.line(r, energy, line_width = 2, legend_label = symbols)
plot.legend.location = "bottom_right"

show(plot)



print(potential.atom_style)
print(potential.charges(['Cl']))



