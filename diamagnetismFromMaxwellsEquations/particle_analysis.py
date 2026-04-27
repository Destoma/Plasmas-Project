import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import h5py
import openpmd_api as io
from functools import partial

# Vacuum Speed of Light
C = 299792458

# Counts the number of time steps (that is, the number of times at which data is generated)
timestep_filenames = os.listdir("data/data/phase_space/x")  # File names identical for each coordinate
num_timesteps = len(timestep_filenames)
frame_plots = {
    'x': [],
    'y': [],
    'z': []
}
pos = {
    'x': [],
    'y': [],
    'z': []
}
vel = {
    'x': [],
    'y': [],
    'z': [],
    'mag': []
}

fig = plt.figure()

for timestep in range(num_timesteps):
    datafile = timestep_filenames[timestep]
    for coord in ['x', 'y', 'z']:
        # Gather raw data for this timestep and coordinate
        raw_data = np.load('data/data/phase_space/' + coord + '/' + datafile)
        num_particles = len(raw_data)
        pos[coord] = np.zeros(num_particles)
        vel[coord] = np.zeros(num_particles)
        for particle in range(num_particles):
            pos[coord][particle] = raw_data[particle][0]
            vel[coord][particle] = raw_data[particle][1]
            # print(f"{pos[coord][particle]}, {vel[coord][particle]}")
        # Store the data for the scatterplot animation
        if timestep < 1e11:       # (timestep < num_timesteps - 1) & (timestep > 0):
            frame_plots[coord].append([np.copy(pos[coord]), np.copy(vel[coord])])
        else:
            path = plt.scatter(pos[coord], vel[coord], label="i forgot", color="black", s=0.1)
            frame_plots[coord].append([np.copy(pos[coord]), np.copy(vel[coord])])
            # plt.show()
            plt.clf()

plt.close()
fig, ax = plt.subplots()
scatter = ax.scatter([0], [0], label="i forgot", color="black", s=0.1)


def update_coord_plot(frame, pos_coord, vel_coord):
    pos = frame_plots[pos_coord][frame][0]
    vel = frame_plots[vel_coord][frame][1]
    points = np.stack([pos, vel]).T
    scatter.set_offsets(points)
    return scatter


#################################################
#   CHOOSE THE PHASE SPACE COMPONENTS TO PLOT   #
#################################################

pos_coord = "x"
vel_coord = "y"

anim = ani.FuncAnimation(fig=fig, func=partial(update_coord_plot, pos_coord=pos_coord, vel_coord=vel_coord), frames=num_timesteps, interval=100, repeat=False)
plt.axis((-5, 5, -C, C))
plt.xlabel(f"Particle {pos_coord}-position")
plt.ylabel(f"Particle {vel_coord}-velocity")
plt.show()
plt.close()


print()