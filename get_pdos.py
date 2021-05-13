from procar import procar_data
import time
from ase import *
from ase.io import read
from ase.calculators.vasp import Vasp
from ase.calculators.vasp import VaspDos
import numpy as np

# Change here
atoms = read('CONTCAR_opt')
#indices = [atom.index for atom in atoms]

C1=[133]
C2=[131]
O=[146]

E_F = -2.3279 #should change in different conditions

emin = -10.
emax = 5
npts = 10001

width = 0.1

#######
procar = procar_data('PROCAR', nspin=1) # ISPIN = 1 then, nspin= 1. ISPIN=2, nspin=2
energies, pdos_d_up_1 = procar.get_partial_dos(emin,emax,npts,width,energy_shift=-E_F,spins=[0],
                                             kpoints=[0],lineshape="Gaussian",atoms=C1,
                                             orbitals='all').T #s, p, d, px, py,pz, dxz, dxy, dx2-y2, dz2, dxy


energies, pdos_d_up_2 = procar.get_partial_dos(emin,emax,npts,width,energy_shift=-E_F,spins=[0],
                                             kpoints=[0],lineshape="Gaussian",atoms=C2,
                                             orbitals='all').T 


energies, pdos_d_up_3 = procar.get_partial_dos(emin,emax,npts,width,energy_shift=-E_F,spins=[0],
                                             kpoints=[0],lineshape="Gaussian",atoms=O,
                                             orbitals='all').T 

#energies, pdos_d_down = procar.get_partial_dos(emin,emax,npts,width,energy_shift=-E_F,spins=[1], kpoints=[0],lineshape="Gaussian",atoms=indices,orbitals='dxy').T

np.savetxt('R_C1.dat' % energies, np.array([energies, pdos_d_up_1]).T, '%.4f %.7f')

np.savetxt('R_C2.dat' % energies, np.array([energies, pdos_d_up_2]).T, '%.4f %.7f')

np.savetxt('R_CHO.dat' % energies, np.array([energies, pdos_d_up_3]).T, '%.4f %.7f')
