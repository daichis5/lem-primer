"""Save the column table of Practice 3 to columns.npz."""

import numpy as np

import columns
import slices

R = slices.Circle().radius
centre = np.array([6.0, 0.0, 18.0])
axis = np.array([0.0, 1.0, 0.0])
col = columns.make_columns(columns.Ellipsoid(centre, (R, 2 * R, R)), 0.5)
columns.save_columns("columns.npz", col, centre, axis)
print(f"{len(col.W)} columns saved to columns.npz")
