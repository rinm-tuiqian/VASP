'''
This script use VDW is re-vdWDF2 not ivdw =11(DFT-D3),meanwhile,functional is not PBE at all. 
'''
from ase.io import read
from ase.calculators.vasp import Vasp, xdat2traj
import numpy as np
import os

name = 'H_Cr2CO2'

n = 0
for file in os.listdir('.'):
    if file.startswith(name):
        if int(file[len(name)+1:len(name)+3]) > n:
            n = int(file[len(name)+1:len(name)+3])
if n > 0:
    atoms = read('%s-%02i.traj' % (name, n))
    print('Read file %s-%02i.traj' % (name, n))
else:
    path = os.getcwd()
    files = os.listdir(path)
    files.sort()
    atoms = read(files[0])

calc = Vasp(prec='Normal',
            xc='PBE',
            gamma=True,
            kpts=[4,4,1],
            encut=400,
            ediff=1E-4,
            nelmin=4,
            algo='Fast',
            lreal='Auto',
            ismear=1,
	        isym=0,
            sigma=0.1,
            ncore=8,
            icharg=1,
            lwave=False,
            ibrion=2,
            nsw=2000,
            ediffg=-0.02,
            luse_vdw=True,
            zab_vdw = -1.8867,
            aggac=0.0,
            gga='MK',
            param1=0.1234,
            param2=0.7114,
            )

atoms.set_calculator(calc)
atoms.get_potential_energy()
n += 1
xdat = xdat2traj(trajectory='%s-%02i.traj' % (name, n), calc=calc)
xdat.convert()

calc.set(ediff=1e-6,
         ibrion=1,
         ediffg=-0.01)
atoms.get_potential_energy()
n += 1
xdat = xdat2traj(trajectory='%s-%02i.traj' % (name, n), calc=calc)
xdat.convert()

E =  atoms.get_potential_energy()
print('Energy for %s : %.4f' % (name, E))

os.system('mv CONTCAR CONTCAR_opt')
os.system('mv OUTCAR OUTCAR_opt')
os.system('rm CHG* D* E* I* OS* P* R* W* a* v* K*')


