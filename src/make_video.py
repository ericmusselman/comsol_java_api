# run as: python make_video.py

import numpy as np
import os
import matplotlib.pyplot as plt

fiber = 0
model = 0

ve_path = os.path.join('..', 've_files', f'model{model}_fiber{fiber}.dat')
print('ve_path: {}'.format(ve_path))
ve = -1*np.loadtxt(ve_path, skiprows=1)

coords_path = os.path.join('..', 'coords_files', f'{fiber}.dat')
coords = np.loadtxt(coords_path, skiprows=1)[:,-1]

fig, ax = plt.subplots()


fig, ax = plt.subplots()
ax.plot(coords, ve, 'k-')
plt.show()
# nnodes = len(ve)
# len_mm = 12.5 # [mm]
# d1Ve = np.diff(ve)/(len_mm/nnodes)
# d2Ve = np.diff(np.diff(ve)/(len_mm/nnodes))/(len_mm/nnodes)  # [mV/mm**2]
# ax.plot(coords[:-1], d1Ve, 'b-')
# ax.plot(coords[:-2], d2Ve, 'g-')
# plt.show()
print('DONE')