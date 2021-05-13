# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:51:07 2021

@author: pengguyue
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,10,2000)
y=np.sin(x)


fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x,y,ls='-',lw=2)


ax.set_ylim(-1.5,1.5)
arrowprops=dict(arrowstyle='->',color='r')
ax.annotate("",(3*np.pi/2,np.sin(3*np.pi/2)+0.05),xytext=(np.pi/2,np.sin(np.pi/2)+0.05),
            color='r',arrowprops=arrowprops)
ax.arrow(0.0,-0.4,np.pi/2,1.2,head_width=0.05,head_length=0.1,fc='g',ec='g')
ax.grid(ls=':',color='gray',alpha=0.5)
plt.show()