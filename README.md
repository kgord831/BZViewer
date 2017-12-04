# BZViewer
Given reciprocal lattice vectors, construct a three dimensional Brillouin Zone.

## How to use it
- Open visualize.py
- Type in the reciprocal lattice vectors b1, b2, and b3 into the list of lattice_vectors
- python visualize.py
- This will generate cad_script.scr
- Open autocad
- *Make sure osnap is turned off!*
- Call `scriptcall` then double-click on the generated cad_script.scr
- Visualize!

## Acknowledgements
Thanks to
http://www.thp.uni-koeln.de/trebst/Lectures/SolidState-2016/wigner_seitz_3d.py
for introducing me to Voroni cells and how to use them to compute Brillouin zones.
