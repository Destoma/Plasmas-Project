import numpy as np
import re

kb = 1.380649e-23
mu = 1.25663706e-6
eps = 8.854e-12
me = 9.10938356e-31
mi = 1 * me   # 1.626e-27
c = 2.99792458e8
q = 1.602e-19
# fundamental constants

x_wind = 10
y_wind = 0.05
z_wind = 0.05
nx = 100
ny = 10
nz = 10
grid_shape = (nx, ny, nz)
# number of grid points

x = np.linspace(-x_wind/2, x_wind/2, nx, dtype=float)
y = np.linspace(-y_wind/2, y_wind/2, ny, dtype=float)
z = np.linspace(-z_wind/2, z_wind/2, nz, dtype=float)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
# define the grid

# Wire Loop Current (A)
current = 15500         # Provides 22 mT at loop center

# Components of the B-field
Bx = np.zeros(grid_shape)
By = np.zeros_like(Bx)
Bz = np.zeros_like(Bx)

print(Bx.shape)
print(By.shape)
print(Bz.shape)


# Read numerically-derived B-field from MATLAB
Bx_raw = open("Bx_raw.txt", "r")
By_raw = open("By_raw.txt", "r")
Bz_raw = open("Bz_raw.txt", "r")

# Translate MATLAB data dump to 1-D numpy arrays with MATLAB indexing
Bx_raw_array = np.asarray(re.split(",|\n", Bx_raw.read())[:-1]).astype(np.float64)
By_raw_array = np.asarray(re.split(",|\n", By_raw.read())[:-1]).astype(np.float64)
Bz_raw_array = np.asarray(re.split(",|\n", Bz_raw.read())[:-1]).astype(np.float64)

# Translate to 3-D B-field Arrays
for x in range(nx):
    for y in range(ny):
        for z in range(nz):
            Bx[x][y][z] = Bx_raw_array[(ny*nz)*x + nz*y + z]
            By[x][y][z] = By_raw_array[(ny*nz)*x + nz*y + z]
            Bz[x][y][z] = Bz_raw_array[(ny*nz)*x + nz*y + z]

# Adjust for current in the wire loop
Bx = current * Bx
By = current * By
Bz = current * Bz

print(f"Maximum Bx: {np.amax(Bx)} T")

# Save Numpy Arrays
np.save('Bx_ex2.npy', Bx)
np.save('By_ex2.npy', By)
np.save('Bz_ex2.npy', Bz)

# Report success
print("External fields generated and saved.")
print(f"Grid size: {nx} x {ny} x {nz}")
print(f"Box dimensions: {x_wind} m x {y_wind} x {z_wind} m")
print(f"Wire Loop Current: {current} A")
