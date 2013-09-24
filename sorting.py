# sorting.py
# This file contains testing and auxiliary functions.

import pylab
import os
import subprocess

# Testing Functions

def isSorted(data):
    """ Returns true if the data is sorted in increasing order. """
    return all( data[i] <= data[i+1] for i in range(len(data)-1) )    



def genData(length=100, maximum=100):
    """ Generates random data given length and maximum. """
    from random import randint
    return [randint(0,maximum) for i in range(length)]
    
def genPermutation(lenght=100):
    """ Generates a random permutation. """
    from random import shuffle
    x = range(lenght)
    shuffle(x)
    return x


def testAlgorithm(algorithm, number=100, length=100, maximum=100):
    """ Tests an algorithm with a number of random inputs. """
    for i in range(number):
        original_data = genData(length,maximum)
        sorted_data = algorithm(original_data, False)
        if not isSorted(sorted_data):
            print "Error! A counterexample was found!"
            print sorted_data
            return False
    return True



# Plotting functions

class Plotter:
    """ Data visualizer. """

    def __init__(self, data, plot=True, folder="./", step=0):
        self.folder = folder
        self.step = step
        self.data = data
        self.plot = plot

    def snapshot(self):
        """ Plots the current data. """
        if self.plot:
            # Saves the current state into plot[step].png.
            pylab.plot(range(len(self.data)),self.data,'k.',markersize=6)
            pylab.savefig("{}plot{:04d}.png".format(self.folder,self.step))
            pylab.clf()
            self.step += 1

    def end(self):
        """ Creates the video. """
        if self.plot:
            # Shell commands. Assuming that avconv is installed.
            # WARNING: It will delete all plot???.png files in the folder. 
            subprocess.call("cd {0}".format(self.folder), shell=True)
            subprocess.call("ffmpeg -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)
            #subprocess.call("avconv -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)
            for f in os.listdir("."): 
                if f.startswith("plot") and f.endswith(".png"): os.remove(f)
