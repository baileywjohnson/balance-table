# balance-table
This project implements a balancing algorithm for placing "blocks" (integers) on/into a "table" (two-dimensional matrix), ensuring the calculated center-of-gravity is not to exceed a range at which the table would fall.

I chose to use [Eel](https://github.com/samuelhwilliams/Eel) to create the GUI which allows users to input a table size and visualizes the placement algorithm in real-time.

To build/run the project on Windows, simply run the CLI/GUI executables at the root of this repository (for GUI, Eel python package is bundled and executable will spawn a Chromium instance, similar to Electron).  On Linux/OS X, either run the Non-GUI.py script or install Eel and run app.py from within the GUI directory.
