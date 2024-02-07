# EXTRA ! - 3D PLOT

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# print(zs_sequence)

# xs = np.arange(-5, 5, 0.25)
# ys  = np.arange(-5, 5, 0.25)

# # Plot the surface.
# surf = ax.plot_surface(xs, ys, zs, linewidth=0, antialiased=False)
# ax.plot(xs, ys, zs)

# plt.show()

from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = g_vect(X, Y)

# Plot the surface.
#surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

sequence = gradient_descent_sequence(g, [0, -3], 0.001, 0.01, 1000)

zs_sequence = g_vect(sequence[0], sequence[1])

ax.scatter3D(sequence[0], sequence[1], zs_sequence, c=zs_sequence, cmap='Greens')

# Customize the z axis.
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-50, 50)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()