# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:53:51 2020

@author: pengg
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:53:51 2020

@author: pengg
be care for atoms size

"""

import numpy as np
from ase.io import write,read
from ase.build import molecule
from ase.data.colors import jmol_colors
from ase.data import covalent_radii



atoms=read('POSCAR')
n=len(atoms)
number=atoms.get_atomic_numbers()
colors=jmol_colors[number]


indice_C = [atom.index for atom in atoms if atom.symbol == 'C']
indice_H = [atom.index for atom in atoms if atom.symbol == 'H']
indice_Cu = [atom.index for atom in atoms if atom.symbol == 'Cu']
indice_O = [atom.index for atom in atoms if atom.symbol == 'O']
indice_N = [atom.index for atom in atoms if atom.symbol == 'N']
indice_Au = [atom.index for atom in atoms if atom.symbol == 'Au']



for i in indice_H:
	colors[i] = [255,250,250] / np.array([255.])
for j in indice_Cu:
	colors[j] = [210,105,30] / np.array([255.])
for k in indice_C:
    colors[k]=[105,105,105]/np.array([255.])
for l in indice_O:
	colors[l]= [255,13,13]/np.array([255.])
for a in indice_Au:
	colors[a]= [255,215,0]/np.array([255.])


radii = covalent_radii[number]
for t in indice_H:
	radii[t] = 0.45
for m in indice_Cu:
	radii[m] = 1.45
for q in indice_C:
	radii[q] = 0.9
for p in indice_O:
	radii[p] = 0.88
for s in indice_N:
	radii[s] = 0.88
for a in indice_Au:
	radii[a] = 1.6



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
   #'colors'        : colors,# List: one (r, g, b) tuple per atom
    'show_unit_cell': 0,   # 0, 1, or 2 to not show, show, and show all of cell  !show lattice!  
    }

# Extra kwargs only available for povray (All units in angstrom)
kwargs.update({
   # 'run_povray'   : True, # Run povray or just write .pov + .ini files this computer is invaild
    'display'      : True, # Display while rendering
   # 'camera_type'  : 'orthographic', # perspective, ultra_wide_angle
    'pause'        : True, # Pause when done rendering (only if display)
  #  'transparent'  : False,# Transparent background if it is ture the background is white
    'canvas_width' : None, # Width of canvas in pixels
    'canvas_height': 1480, # Height of canvas in pixels  !only change one of width and height!
    'colors'       : colors,
    'camera_dist'  : 100.,  # Distance from camera to front atom
    'image_plane'  : None, # Distance from      uyu front atom to image plane
    'camera_type'  : 'orthographic', # perspective, ultra_wide_angle
    'point_lights' : [],    # [[loc1, color1], [loc2, color2],[[[30,30,100],'White'],
                                                                            #[[30,10,100],'White']]]
    'area_light'   : [(30., 10., 60.), # location
                      'White',       # color
                      70.7, 70.7, 50, 60],# width, height, Nlamps_x, Nlamps_y
   # 'background'   : 'White',        # color defult is White
   'transparent'   :'True',
    'textures'     : tex, # Length of atoms list of texture names
    #'rotation'     :rot,
    'celllinewidth': 0.1,  # Radius of the cylinders representing the cell
    })


write('1.pov', atoms,  **kwargs)

rot = ('-30x')#变换 rot = ('-90x,-90y')
kwargs['rotation']=rot
kwargs.update({'canvas_height' :800,})

write('2.pov', atoms, **kwargs) # it will output 2.png 

'''
os.remove('1.pov')
os.remove('1.ini')
os.remove('2.pov')
os.remove('2.ini')

假如我定义一个函数，不能确定参数有多少个，例如要对输入的一组数字做连加操作。那么就可以定义plus(*x)，
当调用该函数时，若输入多个变量plus(1,2,3)，那么就会把输入的变量组合成一个元祖x=(1,2,3)输入。
定义双星号plus(**x)的意思是，调用该函数时若写出形参变量plus(a=1,b=2,c=3)，那么输入变量就会组合成字典x={a:1,b:2,c:3}传入函数。
'''




