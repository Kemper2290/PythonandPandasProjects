
import atomman as am

potential = am.load_lammps_potential(
    id='2011--Zhou-X-W--Li-Na-K-Rb-Cs-F-Cl-Br-I--LAMMPS--ipr1',
    status=None,
    getfiles=True
)

print(potential)
print(potential.charges())
print(potential.pair_style)
print(potential.symbols)
print(potential.pair_info)



