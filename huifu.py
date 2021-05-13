# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:57:19 2021

@author: pengguyue
"""


from ase.io import read
from ase import atoms
from ase.visualize import view

def scale(file_1, file_2):
 atoms0 = read(file_1)
 scaled0 = atoms0.get_scaled_positions(wrap=False)
 
 atoms = read(file_2)
 scaled = atoms.get_scaled_positions(wrap=False)
 for m in range(len(scaled)):
  for i in range(3):
   if scaled[m,i] - scaled0[m,i] > 0.5:
    scaled[m,i] -= 1.
   elif scaled[m,i] - scaled0[m,i] < -0.5:
    scaled[m,i] += 1.
 atoms.set_scaled_positions(scaled)
 atoms.write(file_2)
 return


scale('CONTCAR_IS','CONTCAR_FS')
a=read('CONTCAR_FS')

view(a)