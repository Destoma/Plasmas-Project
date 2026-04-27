import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import h5py
import openpmd_api as io
from functools import partial

fields = io.Series("data/data/fields.h5", io.Access.read_only)
particles = io.Series("data/data/particles.h5", io.Access.read_only)

num_iterations = len(fields.iterations)

print(fields.iterations)
i = fields.iterations[num_iterations - 1]
print(i)

J = i.meshes["J"]
B = i.meshes["B"]

J_x = J["x"]
J_y = J["y"]
J_z = J["z"]
B_x = B["x"]
B_y = B["y"]
B_z = B["z"]

############################################
#   CHOOSE THE B-FIELD COMPONENT TO PLOT   #
############################################
B_x_tot = B_x[:]       # An actual list of data
fields.flush()      # Need to do this, otherwise stuff doesn't exist

B_x_ext = np.load("demos/diamagnetism_ex2_wire_loop/Bx_ex2.npy")
B_y_ext = np.load("demos/diamagnetism_ex2_wire_loop/By_ex2.npy")
B_z_ext = np.load("demos/diamagnetism_ex2_wire_loop/Bz_ex2.npy")

Nx = 100
Ny = 10
Nz = 10

zed = 5

X = np.linspace(0, 10, Nx, dtype="float64")
Y = np.linspace(-0.025, 0.025, Ny, dtype="float64")
Y_3d, X_3d = np.meshgrid(Y, X)

Z = np.zeros((Nx, Ny), dtype="float64")
for x in range(Nx):
    for y in range(Ny):
        Z[x][y] = B_x_tot[x][y][zed] - B_x_ext[x][y][zed]

Z_min = np.amin(Z)
Z_max = np.amax(Z)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
surf = ax.plot_surface(X_3d, Y_3d, Z)
ax.set_zlim(Z_min, Z_max)
plt.show()
plt.close()




# data_on_x_axis = np.zeros(Nx)
# ext_on_x_axis = np.zeros(Nx)
# for i in range(Nx):
#     data_on_x_axis[i] = data[i][int(np.floor(Ny / 2)) + 1][int(np.floor(Nz / 2))]
#     ext_on_x_axis[i] = B_x_ext[i][int(np.floor(Ny / 2))][int(np.floor(Nz / 2))]
# plt.plot(X, data_on_x_axis)
# plt.plot(X, ext_on_x_axis)
# plt.axis((0, 0.5, np.minimum(2 * np.amin(data_on_x_axis), 0), np.maximum(2 * np.amax(data_on_x_axis), 1e-20)))
# plt.xlabel("x-position on x-axis")
# plt.ylabel("B_x")
# plt.show()
# plt.close()
#
# data_on_y_axis = np.zeros(Ny)
# ext_on_y_axis = np.zeros(Ny)
# for i in range(Ny):
#     data_on_y_axis[i] = data[int(np.floor(Nx / 2))][i][int(np.floor(Nz / 2))]
#     ext_on_y_axis[i] = B_x_ext[int(np.floor(Nx / 2))][i][int(np.floor(Nz / 2))]
# plt.plot(Y, data_on_y_axis)
# plt.plot(Y, ext_on_y_axis)
# plt.axis((-0.05, 0.05, np.minimum(2 * np.minimum(np.amin(data_on_y_axis), np.amin(ext_on_y_axis)), -1e-20), np.maximum(2 * np.maximum(np.amax(data_on_y_axis), np.amax(ext_on_y_axis)), 1e-20)))
# plt.xlabel("y-position on y-axis")
# plt.ylabel("B_x")
# plt.show()
# plt.close()
