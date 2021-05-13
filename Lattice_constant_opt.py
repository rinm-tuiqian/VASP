# This script performs the optimization of lattice constant for primitive cell.
# Requires the developer version of ASE

from ase.io import read
import numpy as np
from ase.calculators.vasp import Vasp, xdat2traj
import os
from ase.io.trajectory import Trajectory

name = '' # Write your system

kpts = [16, 16, 1] # Change this based on your initial structure


def get_calc(kpts):
    return Vasp(
        prec='Normal',
        xc='PBE',
        gamma=True,
        kpts=kpts,
        encut=400,
        ediff=1E-4,
        nelmin=5,
        algo='Fast',
        lreal='Auto',
        ismear=1,
        sigma=0.1,
        isym=0,
        icharg=1,
        lwave=False,
        ncore=8,
        ibrion=2,
        nsw=1000,
        ediffg=-0.02,
        # Change the van der Waals interactions below
        gga='MK',    
        luse_vdw=True,
        param1=0.1234,
        param2=0.711357,
        zab_vdw=-1.8867,
        aggac=0.0000,
        lasph=True
    )


atoms = read('ini.traj') # read your initial geometry structure

traj = Trajectory('%s.traj' % name, 'w')
for a in np.arange(atoms.cell[0,0] - 0.2, atoms.cell[0,0] + 0.2, 0.01): # go though gitter parameters around the value in the initial geometry
    cell = atoms.get_cell()
    cell[0] *= a / atoms.cell[0,0]
    cell[1] *= a / atoms.cell[0,0]
    cell[2] *= a / atoms.cell[0,0]
    atoms.set_cell(cell, scale_atoms=True)
    calc = get_calc(kpts)
    atoms.set_calculator(calc)
    n = 0
    
    E = atoms.get_potential_energy()  # Run the optimization with larger convergence limit
    n += 1
    xdat = xdat2traj(trajectory='%.3f-%02i.traj' % (a ,n), calc=calc)
    xdat.convert()

    calc.set(ediff=1e-6,
             ibrion=1,
             ediffg=-0.005,
             # Change the van der Waals interactions below
             gga='MK',
             luse_vdw=True,
    	     param1=0.1234,
   	         param2=0.711357,
 	         zab_vdw=-1.8867,
	         aggac=0.0000,
	         lasph=True)

    atoms.get_potential_energy() # run the more accurate optimization
    n += 1
    xdat = xdat2traj(trajectory='%.3f-%02i.traj' % (a ,n), calc=calc)
    xdat.convert()

    print(a, E)
    calc.clean()
    traj.write(atoms) # Generate a trajectory file with the parabolic relatoin between E and a
traj.close()
