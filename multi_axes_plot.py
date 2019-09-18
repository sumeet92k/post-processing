# -*- coding: utf-8 -*-
#! /usr/bin/python3
# Copyright (c) 2019, sumeet92k
# All rights reserved. Please read the "license.txt" for license terms.
#
# RESULTS FOR: multi axes plot
"""
Calculates interface velocity and average interface undercooling, then plots in a figure with multiple axes
"""

import math
import numpy as np
import matplotlib
matplotlib.rcParams["savefig.directory"] = ""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

dt = 0.014

velocity = []

fname0 = "liquid_contour_phi0.dat"
fname1 = "liquid_contour_phi1.dat"

timestep, count_phi0, T_phi0, pos_phi0 = np.loadtxt(fname0, usecols=(0, 1, 2, 3), unpack=True, skiprows=1)
timestep, count_phi1, T_phi1, pos_phi1 = np.loadtxt(fname1, usecols=(0, 1, 2, 3), unpack=True, skiprows=1)

pos_avg, T_avg = np.zeros(len(timestep)), np.zeros(len(timestep))

f_write = open('velocity_interface.dat', "w")
f_write.write('# total_count\t timestep\t pos_x\t temperature\t velocity \n') 
for i in range(np.size(timestep) - 1):
	pos_avg[i+1] = pos_phi0[i+1]*count_phi0[i+1] + pos_phi1[i+1]*count_phi1[i+1]
	pos_avg[i+1] = pos_avg[i+1]/(count_phi0[i+1] + count_phi1[i+1])
	
	T_avg[i+1] = T_phi0[i+1]*count_phi0[i+1] + T_phi1[i+1]*count_phi1[i+1]
	T_avg[i+1] = T_avg[i+1]/(count_phi0[i+1] + count_phi1[i+1])
	
	pos_avg[i] = pos_phi0[i]*count_phi0[i] + pos_phi1[i]*count_phi1[i]
	pos_avg[i] = pos_avg[i]/(count_phi0[i] + count_phi1[i])
	
	T_avg[i] = T_phi0[i]*count_phi0[i] + T_phi1[i]*count_phi1[i]
	T_avg[i] = T_avg[i]/(count_phi0[i] + count_phi1[i])

	velocity.append( (pos_avg[i+1] - pos_avg[i])/( dt*(timestep[i+1]-timestep[i]) ) )

	f_write.write('{0}\t {1}\t {2:4.5f}\t {3:4.5f}\t {4:4.5f} \n'.format( count_phi0[i] + count_phi1[i], timestep[i], pos_avg[i], T_avg[i], velocity[i] ) )
    
f_write.close()


###================BEGIN Multi axis figures =================###

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Timeteps', fontsize=16)
ax1.set_ylabel('Interface Velocity', fontsize=16, color=color)
ax1.plot( timestep[0:np.size(timestep)-1], velocity, color=color )
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='both', which='major', labelsize=12)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel(r"$ \Delta T $ Undercooling", fontsize=16, color=color)  # we already handled the x-label with ax1
ax2.plot( timestep[0:np.size(timestep)], 1.0-T_avg, color=color )
start, end = ax2.get_ylim()
ax2.yaxis.set_ticks( np.arange(start, end, 0.0005) )
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

###================END Multi axis figures =================###
