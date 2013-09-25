# sorting.py
# This file contains testing and auxiliary functions.

import pylab
import os
import subprocess

class Sorting:
    """ Controls the execution of sorting algorithms. """

    def __init__(self, plot=True, algorithm):
        self.data_length = 80
        self.data_maximum = 80
        self.plot = plot
        self.algorithm = algorithm


    # Auxiliary Functions
    def isSorted(data):
        """ Returns true if the data is sorted in increasing order. """
        return all( data[i] <= data[i+1] for i in range(len(data)-1) )
    
    def genData():
        """ Generates random data. """
        from random import randint
        return [randint(0,self.data_maximum) for i in range(self.data_length)]

    def genPermutation():
        """ Generates a random permutation. """
        from random import shuffle
        x = range(self.data_lenght)
        shuffle(x)
        return x


    # Algorithm control functions
    
    def testAlgorithm(number=100):
        """ Tests an algorithm with a number of random inputs. """
        for i in range(number):
            original_data = genData()
            sorted_data = algorithm(original_data, False)
            if not isSorted(sorted_data):
                print "Error! A counterexample was found!"
                print sorted_data
                return False
            print "The algorithm passed all tests"
            return True

    def plotAlgorithm():
        pass


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

        def createMovie(self):
            """ Creates the video using snapshots. """
            if self.plot:
                # Shell commands. Assuming that avconv is installed.
                # WARNING: It will delete all plot???.png files in the folder. 
                subprocess.call("cd {0}".format(self.folder), shell=True)
                subprocess.call("ffmpeg -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)
                #subprocess.call("avconv -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4", shell=True)
                for f in os.listdir("."): 
                    if f.startswith("plot") and f.endswith(".png"): os.remove(f)
