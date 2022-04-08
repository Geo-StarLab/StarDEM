# PyDEM

An open sourced Discrete Element Method (DEM) software based on Python. 

This is a very simple DEM code for beginners who are interested in DEM coding. 

Due to the low efficiency of Python, it is hard to apply this software to large scale problems which usually involves tons of particles.

## Environment requird
Python 3.x

Post Process : Paraview

## A simple tutorial

Run the "Run_PyDEM.py" file

You will get a results in ResultsOutput file

Use Paraview to check the results as the following steps.

* Open the results.csv file. -> Apply.
* Add the Table To Points filter.
    + Set the X Column, Y Column, and Z Column to the respective columns.
    + Apply.
    + Close the SpreadSheetView. 
* Add the Glyph filter.
    + Change Glyph Type to Sphere.
    + Change Scale Array to the name of the column containing the radius.
    + Change the Scale Factor to 2. (The spheres are scaled from a reference with radius 0.5.)
    + Change Glyph Mode to All Points.
    + Apply.

## Contract
Email: cshang.cimne.upc.edu
