# plotting.py
# This file contains plotting functions.

import matplotlib.pyplot as pyplot
import os
import subprocess
import sorting


# General variables
# 'rate' and 'bars' are defined through plot.py
folder = "./"
step = 0


# Plotting functions
def snapshot():
    """ Plots the current data. """
    global step
    # Saves the previous state into plot[step].png.
    pyplot.savefig("{}plot{:04d}.png".format(folder,step))
    step += 1
    # Puts current state into the Axes object
    pyplot.clf()
    pyplot.axis("off")
    # Checks the plotting mode
    if bars:
        pyplot.bar(range(len(sorting.data)), sorting.data,color ='#2a2a2a', linewidth = 0, align='center')
    else:
        pyplot.plot(range(len(sorting.data)), sorting.data, 'k.', markersize=6)

def swaps(i,j):
    """Adds swaps to the current Axes object."""
    if bars:
        pyplot.bar(j,sorting.data[i],color ='#fe2e2e', linewidth = 0, align='center')
        pyplot.bar(i,sorting.data[j],color ='#fe2e2e', linewidth = 0, align='center')
    else:
        pyplot.plot(j, sorting.data[i], "r.", markersize=6)
        pyplot.plot(i, sorting.data[j], "r.", markersize=6)

def createMovie():
    """ Creates the video using the snapshots. """
    # Shell commands. Assuming that avconv is installed.
    subprocess.call("cd {}".format(folder), shell=True)
    subprocess.call("avconv -r {} -i plot%04d.png movie.mp4".format(rate), shell=True)

def restart():
    """ Restarts the plotting system. """
    # WARNING: It will delete all plot???.png files in the folder.
    global step

    step = 0
    for f in os.listdir("."): 
        if f.startswith("plot") and f.endswith(".png"):
            os.remove(f)
