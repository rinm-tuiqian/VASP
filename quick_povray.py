# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:53:51 2020

@author: pengg
"""

import numpy as np
from ase.io import write,read
from ase.data.colors import jmol_colors
from ase.data import covalent_radii
atoms=read('CONTCAR')
n=len(atoms)
number=atoms.get_atomic_numbers()
colors=jmol_colors[number]

indice_C = [atom.index for atom in atoms if atom.symbol == 'C']
indice_H = [atom.index for atom in atoms if atom.symbol == 'H']
indice_Cu = [atom.index for atom in atoms if atom.symbol == 'Cu']
indice_O =[atom.index for atom in atoms if atom.symbol =='O']
for i in indice_H:
	colors[i] = [255,250,250] / np.array([255.])
for j in indice_Cu:
	colors[j] = [210,105,30] / np.array([255.])
for k in indice_C:
        colors[k]=[105,105,105]/np.array([255.])
for l in indice_O:
	colors[l]= [238,0,0]/np.array([255.])

radii = covalent_radii[number]
for n in indice_H:
	radii[n] = 0.45
for m in indice_Cu:
	radii[m] = 1.45
for q in indice_C:
	radii[q] = 0.9
for r in indice_O:
	radii[r] = 0.88

tex = []
for l in range(len(number)):
	if number[l] == 1:
		tex.append('simple')
	elif number[l] == 6:
		tex.append('glass')
	else:
		tex.append('intermediate') #???????????????????


kwargs = {
    #'rotation'      : rot, # text string with rotation (default='' )
    'radii'         : radii, # float, or a list with one float per atom
   # 'colors'        : colors,# List: one (r, g, b) tuple per atom
    'show_unit_cell': 0,   # 0, 1, or 2 to not show, show, and show all of cell  !show lattice!
    }
# Extra kwargs only available for povray (All units in angstrom)
kwargs.update({
  #'run_povray'   : True, # Run povray or just write .pov + .ini files this computer is invaild
    'display'      : True, # Display while rendering
   # 'camera_type'  : 'orthographic', # perspective, ultra_wide_angle
    'pause'        : True, # Pause when done rendering (only if display)
  #  'transparent'  : False,# Transparent background
    'canvas_width' : None, # Width of canvas in pixels
    'canvas_height': 1480, # Height of canvas in pixels  !only change one of width and height!
    'colors'       : colors,
    'camera_dist'  : 50.,  # Distance from camera to front atom
    'image_plane'  : None, # Distance from front atom to image plane
    'camera_type'  : 'perspective', # perspective, ultra_wide_angle
    'point_lights' : [],             # [[loc1, color1], [loc2, color2],...]
    'area_light'   : [(2., 3., 40.), # location
                      'White',       # color
                      .7, .7, 3, 3], # width, height, Nlamps_x, Nlamps_y
   # 'background'   : 'White',        # color defult is White without background
   'transparent'    :'True',
    'textures'     : tex, # Length of atoms list of texture names
    #'rotation'     :rot,
    'celllinewidth': 0.1,  # Radius of the cylinders representing the cell
    })

write('test_1.pov', atoms, **kwargs)


rot = '-90x, -90y, 0z' #旋转变换
kwargs['rotation']=rot
kwargs.update({'canvas_height' :800,
               })

write('test_2.pov', atoms, **kwargs)





