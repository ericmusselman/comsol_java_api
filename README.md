In your IDE, you will need to add the COMSOL plugins (COMSOL(v5.X)/Multiphysics/plugins/*) and bin/json-20190722.jar to your dependencies

A list of coordinates (x, y, z) is saved as <fiber index>.dat in coords_files/ (i.e., (project_directory)/coords_files/fiber_index.dat). The first line is the number of coordinates:


(integer length of xyz-coords) \n
x [space] y [space] z \n
... for each coordinate ...
EOF

You will need to update the contents of (project_directory)/configs/env/(your_OS).json


Note: As the code is written, create new run configuration files (project_directory/config/runs/run_index.json) for probing FEMs (i.e., FEM_index.mph) at new fiber coordinates (i.e., fiber_index.dat). 

In each run configuration file, by specifying a list of models and a list of fibers to extract potentials, the program gets Ve(x,y,z) for all listed fibers in all listed FEMs. You can pass a list of run indices to your terminal. Feel free to recycle/modify this code for your projects.

Run:

1. cd to (<project_directory>/src/)

2. At your command prompt (e.g., PowerShell for Windows, Terminal for Mac), type:

python extract_potentials.py run_indices

Note: depending on your PATH, you may need to type “python3” instead of “python” in the above command.

Note: potentials written to file are in volts. NEURON extracellular mechanisms expect millivolts!
