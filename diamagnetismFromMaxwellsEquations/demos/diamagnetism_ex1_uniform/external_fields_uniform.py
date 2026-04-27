import numpy as np

kb = 1.380649e-23
mu = 1.25663706e-6
eps = 8.854e-12
me = 9.10938356e-31
mi = 1 * me   # 1.626e-27
c = 2.99792458e8
q = 1.602e-19
# fundamental constants

x_wind = 1
y_wind = 1
z_wind = 1
nx = 50
ny = 10
nz = 10
grid_shape = (nx, ny, nz)
# number of grid points

x = np.linspace(-x_wind/2, x_wind/2, nx, dtype=float)
y = np.linspace(-y_wind/2, y_wind/2, ny, dtype=float)
z = np.linspace(-z_wind/2, z_wind/2, nz, dtype=float)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
# define the grid

# B-field Strength (T)
B0 = 1e-15

# Components of the B-field
Bz = np.zeros(grid_shape)
By = np.zeros_like(Bz)
Bx = B0 * np.ones_like(Bz)

print(Bx.shape)
print(By.shape)
print(Bz.shape)

np.save('Bx_uniform.npy', Bx)
np.save('By_zero.npy', By)
np.save('Bz_zero.npy', Bz)
# save npy arrays

print("External fields generated and saved.")
print(f"Grid size: {nx} x {ny} x {nz}")
print(f"Box dimensions: {x_wind} m x {y_wind} x {z_wind} m")
print(f"Magnetic field strength: {B0} T")

# print(Bx)
# print(By)
# print(Bz)
