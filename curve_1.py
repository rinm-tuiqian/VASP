# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:00:17 2020

@author: pengg

注：此段代码存在硬伤，即使是数据不从0开始但是y轴刻度依旧是以0开始，暂时无法解决这问题。

"""



import numpy as np
import matplotlib.pyplot as plt


def cubic_fit(xco, yco):
    """
    We build a cubic polynomial that satisfies
        f(x0) = y0
        f(x1) = y1
        f'(x0) = 0
        f'(x1) = 0. 顶点斜率为0 
        ，每两个image之间产生一条曲线。这条曲线在每个image的x坐标处导数等于零，便能保证曲线光滑。
        两个数据点功能产生四个等式，三次多项式正好有四个待定系数，最终转化成一个线性方程组求根的问题
    """
    x0, y0 = xco[0], yco[0]
    x1, y1 = xco[1], yco[1]
    A = np.array([
            [x0**3,   x0**2, x0, 1],
            [x1**3,   x1**2, x1, 1],
            [3*x0**2,  2*x0,  1, 0],
            [3*x1**2,  2*x1,  1, 0]])
    b = np.array([y0, y1, 0, 0])
    coeff = np.linalg.solve(A, b)
    xfi = np.linspace(x0, x1, 51)
    yfi = np.polyval(coeff, xfi)
    return xfi, yfi


def add_mep(x, y, label_color, **kwargs):
    #assert len(x) == len(y) == len(label_color)
    react_coord = np.array(x)
    energy = np.array(y)
    energy = energy - energy[0]
    # Draw the line connecting all images
    react_coord_fi = np.array([])
    energy_fi = np.array([])
    for i in range(energy.size-1):
        xfi, yfi = cubic_fit(react_coord[i:i+2], energy[i:i+2])
        react_coord_fi = np.append(react_coord_fi, xfi)
        energy_fi = np.append(energy_fi, yfi)
    axes.plot(react_coord_fi, energy_fi, linewidth=line_width, **kwargs)
    # Add energy levels 添加切线
    #for i, coord in enumerate(react_coord):
     #   label_x = np.array([coord - label_length / 2, coord + label_length / 2])
      #  label_y = np.array([energy[i], energy[i]])
       # axes.plot(label_x, label_y, linewidth=label_width, color=label_color[i])


# Size and resolution of the figure in inches (1 inch = 2.54 cm)
figure_size = (30, 12)
figure_dpi = 400

# Font settings 字体设置
font_size = 24 #字号
#font_family = "Arial" #字体
#font_weight = "bold" #是否加粗

# Axes and spines settings xy 轴范围设定
#ymin = -2.0
#ymax = 2.0
#axes_width = 1.5
#spines_width = 1.5

# Length, width of lines and labels
line_width = 10.0
label_length = 0.5
label_width = 2.5

# Global settings and create the figure
#plt.rc("font", size=font_size, family=font_family, weight=font_weight,)
fig, axes = plt.subplots(figsize=figure_size)

#  输入绘制的数据
"""
add_mep这个函数接受3个args和很多个kwargs。三个args分别是每个image对应的位置（通常设置为等差级数），
每个image的能量，和每个image能级的颜色。剩下的kwargs则指定连接每个image的三次曲线或直线的颜色、线型、图例等。
可加入不同曲线进行对比
"""
#x = [0, 1, 2, 3, 4,5,6,7,8,9,10]
#y = [0, 0, 1.05,0.14,1.21,0.85,1.33,0.62,1.74,1.21,1.21]
a= np.arange(15) #print 0~x-1
x = a
y1=[0,0,0.593,-0.41,0.767,0.075,1.12,0.76,1.42,0.776,1.50,0.97,1.79,1.14,1.14]
#y2 =[0,0,0.83,0.49,0.49]
#y3 =[0,0,0.86,0.44,0.44]
#y4 =[0,0,0.59,-0.41,-0.41]
#y5 =[0,0,0.33,-0.24,-0.24]
#add_mep(x, [0, 3.04, 2.50, 4.34, 2.67],   ["k", "b", "r", "c" ,"m"], color="k", linestyle="-", label="Path-A")
add_mep(x, y1, ["k", "b", "r", "c" ,"m"], color="#1F77B4", linestyle="-")
#add_mep(x, y2, ["k", "b", "r", "c" ,"m"], color="#D31A1B", linestyle="-",label='R-CH2')
#add_mep(x, y3, ["k", "b", "r", "c" ,"m"], color="#838B83", linestyle="-",label='R-Phenyl')
#add_mep(x, y4, ["k", "b", "r", "c" ,"m"], color="#FFA500", linestyle="-",label='R-COO*')
#add_mep(x, y5, ["k", "b", "r", "c" ,"m"], color="k", linestyle="-",label='R-CHO')

#add_mep(x, [0,0,1.07,0.75,0.75], ["k", "b", "r", "c" ,"m"], color="k", linestyle="-")
#dd_mep(x, [0,0,1.05,0.458,0.458], ["k", "b", "r", "c" ,"m"], color="c", linestyle="-.")

#add_mep(x, [0, 0, 0.05,0.17,1.71,0.03,0.09], ["k", "b", "r", "c" ,"m"], color="r", linestyle="-")

#add_mep(x, [0, 2.70, 2.95, 1.35, 2.00],   ["k", "b", "r", "c" ,"m"], color="b", linestyle="-", label="Path-B")

# Adjusting the figures
"""
    边框注释
"""
#axes.set_xlabel("Reaction coordinate", fontsize="large", weight=font_weight)
#axes.set_ylabel("Energy (eV)", fontsize="large", weight=font_weight)

#axes.set_xticks([])
#axes.set_ylim(ymin, ymax)
#axes.tick_params(axis="y", width=axes_width)

# Hide or show borders

#for key in ("top", "bottom", "right"):
    #axes.spines[key].set_visible(False) # x轴不可见
 #   axes.spines[key].set_linewidth(spines_width)

# Left border is always shown

#axes.spines["left"].set_linewidth(spines_width)

# Legend 标签生效
axes.legend(edgecolor="w",fontsize=36,loc=2
            )


print(a)

#for a, b  in zip(x, y1):
 #   plt.text(a, b+0.07,"%s eV" % b, ha='center', va='bottom',fontsize=30
  #           ,color="#1F77B4")

#for a, b  in zip(x, y2):
 #   plt.text(a, b+0.07,"%s eV" % b, ha='center', va='bottom',fontsize=30
  #           ,color="#D31A1B")
# Save the figure
fig.tight_layout() #紧密排布 
axes.axis('off')

fig.show('mep_curve.png')
fig.savefig("mep_curve.png", transparent=True,dpi=figure_dpi)
