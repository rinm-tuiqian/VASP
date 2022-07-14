# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:57:02 2020

@author: pengg
ase gui  CONTCAR_opt
"""
from ase.io import read, write
from ase.visualize import view

a=read('CONTCAR_opt')
view(a)
