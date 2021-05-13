# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:11:05 2021

@author: pengguyue
"""
from ase import *
from ase.io import read, write
from ase.constraints import *
import numpy as np
from ase.visualize import view


def sort_atom(atoms):
  atom_list = []
  top_down_list = []
  zmin = 0.0
  zmax = 0.0
  for a in atoms:
    if a.z < zmin:
      zmin = a.z
    elif a.z > zmax:
      zmax = a.z

  for atom in atoms:
    assert(zmax >= atom.z >= zmin)
    atom_pos = np.round(atom.position.copy(),2)
    temp = (atom_pos[2],atom_pos[1],atom_pos[0],atom.index)
    atom_list.append(temp)

  atom_list.sort()

  for a in atom_list:
    top_down_list.append(a[3])

  new_atoms = atoms[top_down_list].copy()
  return new_atoms



#sort_atom('CONTCAR_IS')
atoms = read('CONTCAR_IS')
new_atoms = sort_atom(atoms)
#a=sort_atom('CONTCAR_IS')
view(new_atoms)