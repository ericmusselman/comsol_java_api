import numpy as np
import os
from typing import List

fiber_length = 12500 # [um]
delta_zs = 5 # [um]
x, y = 0, 0
fiber_index = 99

def write(x_coord: float, y_coord: float, z_coords: List[float], path: str):
    """
    :param path:
    """
    with open(path, 'w') as f:
        f.write(str(len(z_coords)) + ' ')
        f.write("\n")
        for row in z_coords:
            if not isinstance(row, int):
                f.write(str(x) + ' ' + str(x) + ' ' + str(row))
            f.write("\n")

z_top_half = np.arange(fiber_length / 2, fiber_length + delta_zs, delta_zs)
z_bottom_half = -np.flip(z_top_half) + fiber_length
while z_top_half[-1] > fiber_length:
    # trim top of top half
    z_top_half = z_top_half[:-1]
    z_bottom_half = z_bottom_half[1:]

fiber_z = np.concatenate((z_bottom_half[:-1], z_top_half), axis=None)
coords_dest = os.path.join('..', 'coords_files', f"{fiber_index}.dat")
print('max: {}'.format(np.max(fiber_z)))
print('min: {}'.format(np.min(fiber_z)))
print('coords_dest: {}'.format(coords_dest))
write(x, y, fiber_z, coords_dest)
