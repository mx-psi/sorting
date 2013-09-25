# plotting.py
# This file contains plotting functions.

import pylab
import os
import subprocess


# General variables
folder = "./"
step = 0

# Plotting functions
def snapshot():
    """ Plots the current data. """
    # Saves the current state into plot[step].png.
    pylab.plot(range(len(sorting.data)), sorting.data, 'k.', markersize=6)
    pylab.savefig("{}plot{:04d}.png".format(folder,step))
    pylab.clf()
    step += 1

def createMovie():
    """ Creates the video using the snapshots. """
    # Shell commands. Assuming that avconv is installed.
    subprocess.call("cd {0}".format(folder), shell=True)
    subprocess.call("ffmpeg -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)
    #subprocess.call("avconv -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)

def restart():
    # WARNING: It will delete all plot???.png files in the folder.
    step = 0
    for f in os.listdir("."): 
        if f.startswith("plot") and f.endswith(".png"):
            os.remove(f)

    
