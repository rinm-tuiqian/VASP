PER_Au = [-383.05997937,-382.10719999,-382.28716013]
PER_Ag = [-131.46505392,-131.08242876,-131.18462938]
PER_Au_pro = PER_Au - np.array(PER_Au[0])
PER_Ag_pro = PER_Ag - np.array(PER_Ag[0])
PER_coordinate = np.arange(len(PER_Au))
fig, PER_Au_fig = plt.subplots(1,1,figsize=(10,5))
plot_curve_up(PER_coordinate, PER_Au_pro, color='orange', path_label='Au(111)',Textlabel='True')
plot_curve_down(PER_coordinate, PER_Ag_pro, color='gray', path_label='Ag(111)',Textlabel='True')
PER_Au_fig.set_ylim([-0.1,1.1])
PER_Au_fig.set_xlabel('Reaction coordinate')
PER_Au_fig.set_ylabel('Energy (eV)')
plt.legend(loc='upper left')
plt.close()
