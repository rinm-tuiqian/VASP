import ase.io as io
import numpy as np
from ase.data import colors
from ase.io import read,write
import os
from ase.build import molecule
from ase.data.colors import jmol_colors
from ase.data import covalent_radii
atoms = read('CONTCAR')

n=len(atoms)
number=atoms.get_atomic_numbers()
colors=jmol_colors[number]

indice_C = [atom.index for atom in atoms if atom.symbol == 'C']
indice_H = [atom.index for atom in atoms if atom.symbol == 'H']
indice_N = [atom.index for atom in atoms if atom.symbol == 'N']
indice_Cu = [atom.index for atom in atoms if atom.symbol == 'Cu']
indice_O = [atom.index for atom in atoms if atom.symbol == 'O']
indice_Au = [atom.index for atom in atoms if atom.symbol == 'Au']
indice_Ag = [atom.index for atom in atoms if atom.symbol == 'Ag']


radii = covalent_radii[number]
for a in indice_H:
	radii[a] = 0.6
for b in indice_C:
	radii[b] = 0.95
for c in indice_O:
	radii[c]= 0.85
for d in indice_Au:
	radii[d]= 1.45
for e in indice_N:
	radii[e]= 1.0
for f in indice_Ag:
	radii[f]= 1.3
#ghij

tex = []
for k in range(len(number)):
	if number[k] == 1:
		tex.append('simple')
	elif number[k] == 6:
		tex.append('glass')
	else:
		tex.append('intermediate') #???????????????????
#lm

for n in indice_H:
	colors[n] = [255,250,255] / np.array([255.])
for o in indice_Cu:
	colors[o] = [105,105,105] / np.array([255.]) #
for p in indice_C:
    colors[p]=[169,169,169]/np.array([255.])  #灰色69,169,169
for q in indice_O:
	colors[q]= [255,0,0]/np.array([255.])#红色
for r in indice_Au:
	colors[r]= [255,215,0]/np.array([255.])#红色
for s in indice_Ag:
	colors[s]= [105,105,105]/np.array([255.])#红色

#colors[945:1260]=[169,169,169] / np.array([255.])
'''
colors[99:143]=[105,105,105] / np.array([255.]) 
colors[321:343]=[105,105,105] / np.array([255.]) 
colors[543:587]=[105,105,105] / np.array([255.]) 
colors[765:787]=[105,105,105] / np.array([255.]) 
colors[910:921]=[105,105,105] / np.array([255.]) 
#colors[]=[105,105,105] / np.array([255.]) 
'''


# Define the atomic bonds to show

#kwargs = {
    #'rotation'      : rot, # text string with rotation (default='' )
     # float, or a list with one float per atom
   # 'colors'        : colors,# List: one (r, g, b) tuple per atom
  #  'show_unit_cell': 0,   # 0, 1, or 2 to not show, show, and show all of cell  !show lattice!
 #   }
renderer = io.write('3.pov', atoms,
                    #rotation='90y',
                    radii=radii,
                    show_unit_cell=0,
                    povray_settings=dict(
                                        
    bondlinewidth=0.07,
    display= True, # Display while rendering
   #camera_type  = ultra_wide_angle, # perspective, ultra_wide_angle
    pause  = True, # Pause when done rendering (only if display)
    transparent  = False,# Transparent background if it is ture the background is white
    canvas_width = None, # Width of canvas in pixels
    canvas_height= 1480, # Height of canvas in pixels  !only change one of width and height!
    colors       = colors,
    camera_dist  = 100.,  # Distance from camera to front atom
    image_plane  = None, # Distance from      uyu front atom to image plane
    camera_type  = 'orthographic', # perspective, ultra_wide_angle，orthographic
    point_lights = [],             # [[loc1, color1], [loc2, color2],...]
    area_light   = [(10., 10., 40.),# location
                      'White',       # color
                      25, 25, 20, 20], # width, height, Nlamps_x, Nlamps_y
    background   = 'White',        # color defult is White
   
    textures     = tex, # Length of atoms list of texture names
    #rotation     =rot,
   # show_unit_cell=False,
    #celllinewidth= 0,
    
    )
    )



