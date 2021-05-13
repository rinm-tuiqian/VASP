import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Function: Autolabel the values of bars in the bar chart
def autolabel(fig, rects, center, offset, size):
	for rect in rects:
		height =rect.get_height()
		if height > 0:
				fig.annotate('%.2f' % height,
							xy=(rect.get_x() + rect.get_width() / 2, height),
							xytext=(center, offset),
							textcoords='offset points',
							fontsize=size,
							ha='center', va='bottom')
		else:
				fig.annotate('%.2f' % height,
							xy=(rect.get_x() + rect.get_width() / 2, height-0.08),
							xytext=(center, offset),
							textcoords='offset points',
							fontsize=size,
							ha='center', va='bottom')

# Dashed line profile
def line_state(x,y,color,Textlabel,path_label,FontSize=20):
	y_new = []
	x_new = []
	for i in range(len(y)):
		y_new.append(y[i])
		y_new.append(y[i])
		x_new.append(2*i+1)
		x_new.append(2*i+2)

	i = 0
	while i < len(y_new):
		x_line = [x_new[i], x_new[i+1]]
		y_line = [y_new[i], y_new[i+1]]
		plt.plot(x_line, y_line, linestyle='-', linewidth=2, color=color,label=path_label)
		i += 2
	if Textlabel == 'True':
		for j in range(len(x)):
			plt.text(x_new[j] * 2 - 1.0, y[j] + 0.05, "{:.2f}".format(y[j]), fontsize=FontSize, color=color)
	return x_new, y_new

def plot_line(x,y,color,path_label,Textlabel,FontSize=20):
   	y_min = min(y)
   	y_max = max(y)
   	y_bias = (y_max - y_min) / 50.
   	
   	x_new, y_new = line_state(x,y,color,path_label='',Textlabel='False')
   	plt.plot(x_new, y_new, linestyle='--', linewidth=2, color=color, label=path_label)
   	if Textlabel == 'True':
   		for j in range(len(x)):
   			plt.text(x_new[j] * 2 - 0.8, y[j] + y_bias, "{:.2f}".format(y[j]), fontsize=FontSize, color=color)
   	
   	plt.gca().axison = False
   	plt.xticks([])
   	plt.yticks([])

# Curve line profile
def cos_curve(y_min, y_max, direction):
	if direction == 'up':
		x_up = np.linspace(np.pi, 2 * np.pi, 50)
		y_curve = [y_min + (y_max - y_min) * (j + 1) / 2 for j in np.cos(x_up).tolist()]
	else:
		x_down = np.linspace(0, np.pi, 50)
		y_curve = [y_min + (y_max - y_min) * (j + 1) / 2 for j in np.cos(x_down).tolist()]
	return y_curve

def cos_interpolate(x, y):
	x_new = []
	y_smooth = []

	x_pre_temp = np.linspace(x[0] - 0.6, x[0], 50).tolist()
	y_pre_temp = np.linspace(y[0], y[0], 50).tolist()
	x_new = x_new + x_pre_temp
	y_smooth = y_smooth + y_pre_temp

	for i in range(len(x) - 1):
		x_new_temp = np.linspace(x[i], x[i+1], 50).tolist()
		if y[i] < y[i+1]:
			y_smooth_temp = cos_curve(y[i], y[i+1], "up")
		else:
			y_smooth_temp = cos_curve(y[i+1], y[i], 'down')
		x_new = x_new + x_new_temp
		y_smooth = y_smooth + y_smooth_temp

	x_post_temp = np.linspace(x[-1], x[-1] + 0.5, 50).tolist()
	y_post_temp = np.linspace(y[-1], y[-1], 50).tolist()
	x_new = x_new + x_post_temp
	y_smooth = y_smooth + y_post_temp

	return x_new, y_smooth

def plot_curve(x, y, color, path_label, Textlabel, FontSize=16):
	x_new_array = []
	y_smooth_array = []

	#plt.subplots(1,1,figsize=(14,4))
	#plt.scatter(x, y, linewidth=2, color=color)
	x_new, y_smooth = cos_interpolate(x, y)
	plt.plot(x_new, y_smooth, linewidth=3.5, label=path_label, color=color)

	if Textlabel == 'True':
		text_ini = plt.text(x[0]-0.5, y[0]+0.1, '{:.2f} eV'.format(y[0]), fontsize=FontSize, color=color)
		text_fin = plt.text(x[-1], y[-1]+0.1, '{:.2f} eV'.format(y[-1]), fontsize=FontSize, color=color)
		for i in range(1, len(x)-1):
			if y[i]  < y[i+1]:
				text = [plt.text(x[i]-0.25, y[i]-0.1, '{:.2f} eV'.format(y[i]), fontsize=FontSize, color=color)]
			else:
				text = [plt.text(x[i]-0.25, y[i]+0.1, '{:.2f} eV'.format(y[i]), fontsize=FontSize, color=color)]


	plt.legend([])
	#plt.gca().axison = False # Turn off the axis
	plt.xticks([])
	plt.yticks([])

def plot_curve_inverse(x, y, color, path_label, Textlabel, FontSize=16):
	x_new_array = []
	y_smooth_array = []

	#plt.subplots(1,1,figsize=(14,4))
	#plt.scatter(x, y, linewidth=2, color=color)
	x_new, y_smooth = cos_interpolate(x, y)
	plt.plot(x_new, y_smooth, linewidth=3.5, label=path_label, color=color)

	if Textlabel == 'True':
		text_ini = plt.text(x[0]-0.5, y[0]+0.05, '{:.2f} eV'.format(y[0]), fontsize=FontSize, color=color)
		text_fin = plt.text(x[-1], y[-1]+0.15, '{:.2f} eV'.format(y[-1]), fontsize=FontSize, color=color)
		for i in range(1, len(x)-1):
			if y[i] > y[i+1]:
				text = [plt.text(x[i]-0.25, y[i]-0.3, '{:.2f} eV'.format(y[i]), fontsize=FontSize, color=color)]
			else:
				text = [plt.text(x[i]-0.25, y[i]+0.15, '{:.2f} eV'.format(y[i]), fontsize=FontSize, color=color)]


	plt.legend([])
	#plt.gca().axison = False # Turn off the axis
	plt.xticks([])
	plt.yticks([])

def plot_curve_down(x, y, color, path_label, Textlabel, FontSize=16,**kwargs):
	x_new_array = []
	y_smooth_array = []

	#plt.subplots(1,1,figsize=(14,4))
	#plt.scatter(x, y, linewidth=2, color=color)
	x_new, y_smooth = cos_interpolate(x, y)
	plt.plot(x_new, y_smooth, linewidth=3, label=path_label, color=color)

	if Textlabel == 'True':
		text_ini = plt.text(x[0]-0.4, y[0]-0.1, '{:.2f} eV'.format(y[0]), fontsize=FontSize, color=color)
		text_fin = plt.text(x[-1], y[-1]-0.1, '{:.2f} eV'.format(y[-1]), fontsize=FontSize, color=color)
		for i in range(1, len(x)-1):
			text = [plt.text(x[i]-0.1, y[i]-0.15, '{:.2f} eV'.format(y[i]), fontsize=FontSize, color=color)]
		
	plt.legend()
	#plt.gca().axison = False
	plt.xticks([])
	plt.yticks([])

def plot_curve_up(x, y, color, path_label, Textlabel, FontSize=16,**kwargs):
	x_new_array = []
	y_smooth_array = []

	#plt.subplots(1,1,figsize=(14,4))
	#plt.scatter(x, y, linewidth=2, color=color)
	x_new, y_smooth = cos_interpolate(x, y)
	plt.plot(x_new, y_smooth, linewidth=3, label=path_label, color=color)
	if Textlabel == 'True':
		text_ini = plt.text(x[0]-0.4, y[0]+0.05, '{:.2f} eV'.format(y[0]), fontsize=FontSize, color=color)
		text_fin = plt.text(x[-1], y[-1]+0.05, '{:.2f} eV'.format(y[-1]), fontsize=FontSize, color=color)
		for i in range(1, len(x)-1):
			text = [plt.text(x[i]-0.08, y[i]+0.05, '{:.2f} eV'.format(y[i]), fontsize=FontSize, color=color)]

	plt.legend()
	#plt.gca().axison = False
	plt.xticks([])
	plt.yticks([])


# Gibbs free energy profile
class ED:
	def __init__(self, aspect='equal'):
		self.ratio = 1.6181
		self.dimension = 'auto'
		self.space = 'auto'
		self.offset = 'auto'
		self.offset_ratio = 0.02
		self.color_bottom_text = 'black'
		self.aspect = aspect

		self.pos_number = 0
		self.energies = []
		self.positions = []
		self.colors = []
		self.top_texts = []
		self.bottom_texts = []
		self.links = []
		self.ls = []
		self.label = []
		self.lw = []

		self.fig = None
		self.ax = None

	def states(self, energy, bottom_text='', position=None, color='k',top_text='',ls='solid',
		label='',lw=2.0):

		if position is None:
			position = self.pos_number + 1
			self.pos_number += 1
		elif position == 'stay':
			position = self.pos_number
		if top_text == 'Energy':
			top_text = energy

		link = []

		self.colors.append(color)
		self.energies.append(energy)
		self.positions.append(position)
		self.top_texts.append(top_text)
		self.bottom_texts.append(bottom_text)
		self.links.append(link)
		self.ls.append(ls)
		self.label.append(label)
		self.lw.append(lw)

	def link(self, start_level, end_level, color='k', ls='--', linewidth=2):
		self.links[start_level].append((end_level,ls,linewidth,color))

	def _auto_adjust(self):
		Energy_variation = abs(max(self.energies) - min(self.energies))
		if self.dimension == 'auto' or self.space == 'auto':
			unitque_positions = float(len(set(self.positions)))
			space_for_level = Energy_variation * self.ratio/unitque_positions
			self.dimension = space_for_level * 0.9
			self.space = space_for_level * 0.3

		if self.offset == 'auto':
			self.offset = Energy_variation * self.offset_ratio

	def plot(self,figsize,ylim):
		matplotlib.rc('xtick',labelsize=18)
		matplotlib.rc('ytick',labelsize=18)
		font = {'family':'DejaVu Sans',
				'size':14}
		matplotlib.rc('font',**font)

		fig = plt.figure(figsize=figsize)
		ax = fig.add_subplot(111, aspect=self.aspect)
		ax.set_xlabel('Reaction Coordinate',fontsize=18)
		ax.set_ylabel('$\mathrm{\Delta G}$ (eV)',fontsize=18)
		ax.axes.get_xaxis().set_visible(True)
		ax.set_xticks([])
		ax.set_ylim(ylim)
		ax.spines['top'].set_visible(True)
		ax.spines['right'].set_visible(True)
		ax.spines['bottom'].set_visible(True)


		self._auto_adjust()

		data = zip(self.energies, #0
				   self.positions, #1
				   self.bottom_texts, #2
				   self.top_texts, #3
				   self.colors, #4
				   self.ls, #5
				   self.label, #6
				   self.lw) #7

		for level in data:
			start = level[1]*(self.dimension+self.space)
			ax.hlines(level[0], start, start+ self.dimension, color=level[4],
					linestyle=level[5],label=level[6],linewidth=level[7])
			ax.text(start + self.dimension / 2.,
					level[0] - self.offset,
					level[2],
					horizontalalignment='center',
					verticalalignment='top',
					color=level[4])

			ax.text(start + self.dimension/2.,
					level[0] + self.offset*3,
					level[3],
					horizontalalignment='center',
					verticalalignment='top',
					color=level[4])

		for idx, link in enumerate(self.links):
			for i in link:
				start = self.positions[idx] * (self.dimension+self.space)
				x1 = start + self.dimension
				x2 = self.positions[i[0]]*(self.dimension+self.space)
				y1 = self.energies[idx]
				y2 = self.energies[i[0]]
				line = Line2D([x1, x2], [y1, y2],
							  ls=i[1],
							  linewidth=i[2],
							  color=i[3])
				ax.add_line(line)
				ax.axvline(x=(x2 + x1)/2, ls='--', color='k')


		ax.legend(fontsize=18)
		self.ax = ax
		self.fig = fig

# add a gradient background for the plot
def gradient_image(ax, extent, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    Draw a gradient image based on a colormap.

    Parameters
    ----------
    ax : Axes
        The axes to draw on.
    extent
        The extent of the image as (xmin, xmax, ymin, ymax).
        By default, this is in Axes coordinates but may be
        changed using the *transform* kwarg.
    direction : float
        The direction of the gradient. This is a number in
        range 0 (=vertical) to 1 (=horizontal).
    cmap_range : float, float
        The fraction (cmin, cmax) of the colormap that should be
        used for the gradient, where the complete colormap is (0, 1).
    **kwargs
        Other parameters are passed on to `.Axes.imshow()`.
        In particular useful is *cmap*.
    """
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, extent=extent, interpolation='bicubic',
                   vmin=0, vmax=1, **kwargs)
    return im


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
line_width = 10.0
figure_size = (30, 12)
figure_dpi = 400
label_length = 0.5
label_width = 2.5
fig, axes = plt.subplots(figsize=figure_size)
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


