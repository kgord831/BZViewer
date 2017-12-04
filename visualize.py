import numpy as np, numpy.linalg as npl
from scipy.spatial import Voronoi
from itertools import product
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# The lattice unit vectors
# unit_vectors = [np.array([-1, 1, 1]), np.array([1, -1, 1]), np.array([1, 1, -1])]
# Simple cubic
# lattice_vectors = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
# 191
# lattice_vectors = [np.array([1, 1./np.sqrt(3), 0]), np.array([0, 2./np.sqrt(3), 0]), np.array([0, 0, 1])]
# fcc
lattice_vectors = [np.array([-0.5, 0.5, 0.5]), np.array([0.5, -0.5, 0.5]), np.array([0.5, 0.5, -0.5])]

# lattice vectors in all directions
latt = []
prefactors = [0., -1., 1.]

for p in prefactors:
	for u in lattice_vectors:
		latt.append(p * u)

# All vectors making up the lattice
lattice = []

# Pick three vectors and build sum
for vs in product(latt, latt, latt):
	a = vs[0] + vs[1] + vs[2]

	# Check if vector is already in lattice
	if not any((a == x).all() for x in lattice): 
		lattice.append(a)

# Create matplotlib figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
lattice = np.array(lattice)
# Display all lattice points
#ax.plot(lattice[:,0], lattice[:,1], lattice[:,2], '+')

# Compute Voronoi diagram from lattice points
voronoi = Voronoi(lattice)

# Iterate over ridges provided by Voronoi and filter if ridge belongs to
# Voronoi cell around the centre point (0., 0., 0.) which has index 0 
surfaces = []
t = 0
for i, points in enumerate(voronoi.ridge_points):
	if points[0] == 0 or points[1] == 0:

		# draw enclosing line
		xs = []
		ys = []
		zs = []

		for j in voronoi.ridge_vertices[i]:
			xs.append(voronoi.vertices[j][0])
			ys.append(voronoi.vertices[j][1])
			zs.append(voronoi.vertices[j][2])

		# add origin of line to ensure a closed polygon
		xs.append(xs[0])
		ys.append(ys[0])
		zs.append(zs[0])

		# display line
		surfaces.append(np.transpose(np.array([xs,ys,zs])))
		t = t + 1

# output script
pairs = []
output_file = "cad_script.scr"
with open(output_file, "w") as f:
	f.write(";Draw the lines for the surfaces\n")
	for s in surfaces:
		f.write("._3dpoly" + '\n')
		(rows,cols) = s.shape
		for i in range(rows - 1):
			f.write("%.4f,%.4f,%.4f%s" % (s[i,0],s[i,1],s[i,2],'\n'))
		f.write("close\n")
	f.write(";Create surface out of the lines\n")
	f.write("ai_selall\n")
	f.write("convtosurface\n")
	f.write(";Convert surfaces to a 3D object\n")
	f.write("ai_selall\n")
	f.write("surfsculpt\n")