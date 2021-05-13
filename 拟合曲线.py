# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:06:28 2021

@author: pengguyue
"""


import numpy as np
import matplotlib.pyplot as plt
#定义x、y散点坐标
#x = [0.95,0.96,0.97,0.98,0.99,1,1.01,1.02,1.03,1.04,1.05,]
#选择读取文件的名称
a = np.loadtxt('SUMMARY_NO.dat',usecols=0,unpack=True,dtype=None)
x = np.array(a)
print('x is :\n',x) #\n  meaning print date in next array
num= np.loadtxt('SUMMARY_NO.dat',usecols=2,unpack=True,dtype=None)
y = np.array(num)
print('y is :\n',y)

#用3次多项式拟合
f1 = np.polyfit(x, y, 3)
print('f1 is :\n',f1)
p1 = np.poly1d(f1)
print('p1 is :\n',p1)
yvals=np.polyval(f1, x)
yvals = p1(x)  #拟合y值
print('yvals is :\n',yvals)


#绘图
plot1 = plt.plot(x, y, 's')#label='original values')
plot = plt.plot(x, yvals, 'r')#label='polyfit values')
plt.xlabel('crystal ')
plt.ylabel('$\mathrm{E}$ (eV)')
#plt.legend(loc=4) 
#指定legend的位置右下角
plt.title('polyfitting')
plt.show()