# plotting.py
# This file contains plotting functions.

import matplotlib.pyplot as pyplot
import os
import subprocess
import sorting



# General variables
folder = "./"
step = 0



# Plotting functions
def snapshot():
    """ Plots the current data. """
    global step

    # Saves the current state into plot[step].png.
    pyplot.clf()
    pyplot.axis("off")
    pyplot.plot(range(len(sorting.data)), sorting.data, 'k.', markersize=6)
    pyplot.savefig("{}plot{:04d}.png".format(folder,step))
    step += 1

def createMovie():
    """ Creates the video using the snapshots. """
    # Shell commands. Assuming that avconv is installed.
    subprocess.call("cd {0}".format(folder), shell=True)
    subprocess.call("ffmpeg -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)
    #subprocess.call("avconv -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)

def restart():
    """ Restarts the plotting system. """
    # WARNING: It will delete all plot???.png files in the folder.
    global step

    step = 0
    for f in os.listdir("."): 
        if f.startswith("plot") and f.endswith(".png"):
            os.remove(f)
