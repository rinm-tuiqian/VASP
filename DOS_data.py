import sys
import numpy as np
import matplotlib.pyplot as plt
class dos_file:
	#split the dos file into several lists for further visualization.
	#calculate the center of the given orbital.
	def __init__(self, name):
		self.name = name

	def dos_list(self, emin, emax, nspin):
		f = open(self.name, 'r')
		if nspin == 1:
			Sum = 0
			fill = 0
			dos = []
			E = []
			for line in f:
				if line.startswith('#'):continue
				E_i, dos_i = float(line.split()[0]), float(line.split()[1])
				dos.append(dos_i)
				E.append(E_i)

				if emin < E_i < emax:
					Sum += E_i * dos_i
					fill += dos_i
			center = Sum / fill	 
			#print ('Center of DOS is: %.5f eV' % center)
			return (E, dos, center)

		elif nspin == 2:
			Sum = 0
			fill = 0
			E = []
			dos_up = []
			dos_down = []
			for line in f:
				line = line.strip()
				if line.startswith('#'):continue
				E_i, dos_up_i, dos_down_i = float(line.split()[0]), float(line.split()[1]), float(line.split()[2])
				E.append(E_i)
				dos_up.append(dos_up_i)
				dos_down.append(dos_down_i)

				if emin < E_i < emax:
					Sum += E_i * (dos_up_i - dos_down_i)
					fill += (dos_up_i - dos_down_i)
			center = Sum / fill
			#print ('Center of DOS is: %.5f eV' % center)
			return E, dos_up, dos_down, center		
		else:
			print ('Wrong spin-polarization!')
			sys.exit(0)
		f.close()
def read_COHP(name):
	f = open(name, 'r')
	E = []
	COHP = []

	for line in f:
		line = line.strip()
		if line.startswith('#'):continue

		E_i = float(line.split()[0])
		COHP_i = float(line.split()[1])
		E.append(E_i)
		COHP.append(COHP_i)
	return E, COHP
	f.close()
	
fig, ax = plt.subplots(1,1,figsize=(8,6))	

R_COOH=dos_file('C:/Users/pengg/Desktop/C2/IS/all/R_COOH.dat').dos_list(-5, 5, 1)
R_OH=dos_file('C:/Users/pengg/Desktop/C2/IS/all/R_OH.dat').dos_list(-5, 5, 1)
R_CHO=dos_file('C:/Users/pengg/Desktop/C2/IS/all/R_CHO.dat').dos_list(-5, 5, 1)

COOH=ax.plot(R_COOH[0],R_COOH[1],c='b',label='R_COOH',linewidth=2,)
OH=ax.plot(R_OH[0],R_OH[1],c='r',label='R_OH',linewidth=2)
CHO=ax.plot(R_CHO[0],R_CHO[1],c='g',label='R_CHO', linewidth=2)


ax.set_xlabel('$\mathrm{E-E_F}$ (eV)')
ax.set_ylabel('DOS (a.u.)')
ax.axvline(x=0,ls='--',c='k')
ax.set_xlim([-6,1.5]) 
ax.set_ylim([0,1.0])
ax.legend(loc='upper left',fontsize=18)
ax.set_title('C2_all DOS') ####title
fig.tight_layout()
plt.savefig('C:/Users/pengg/Desktop/C2/IS/all/fig.png',dpi=300)
plt.show()