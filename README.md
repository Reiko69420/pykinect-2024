# PyKinect2 - Forked

Enables writing Kinect applications, games, and experiences using Python.  Inspired by the original [PyKinect project on CodePlex](http://pytools.codeplex.com/wikipage?title=PyKinect).

Only color, depth, body and body index frames are supported in this version. 
You have some example code in the Examples foleder and the code is pretty easy to read


## Prerequisites

The easiest way to get most of the pre-requisites is to use Anaconda which includes NumPy.  You'll then need to pip install comtypes.  The PyKinectBodyGame sample requires PyGame which needs to be manually installed.

1. Download [Python3.12.3](https://www.python.org/downloads/release/python-3123/)
2. pip install comtypes
3. Install the [Kinect for Windows Runtime 2.2.1811](https://www.microsoft.com/en-us/download/details.aspx?id=57578)
4. Install the [Kinect SDK 2.0](https://www.microsoft.com/en-us/download/details.aspx?id=44561)
5. Go to the file folder > Kinect for Windows Runtime 2.2.1811 > Right click and Install the file “kinectsensor.inf”
6. Then install the Kinect SDK
7. Then run the program KinectRuntime-x64.msi

Full List of Dependencies
* [NumPy](http://www.numpy.org/) 
* [comtypes](https://github.com/enthought/comtypes/) 
* [PyGame](http://www.pygame.org) - for running PyKinectBodyGame sample 

## Installation

The package needs to be installed manually, so first clone/download the project somewhere on your computer,
Go inside it trough your cmd, and type this:
```
pip install .
````
If you are using a virtual environment, be sure to activate it first.

