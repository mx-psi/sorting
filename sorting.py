# sorting.py
# This file contains testing and auxiliary functions.

import pylab
import os
import subprocess


# General variables
data = []
data_length = 80 
data_maximum = 80
algorithm = None
plot = False



# Auxiliary functions

def isSorted(self, data):
    """ Returns true if the data is sorted in increasing order. """
    return all( data[i] <= data[i+1] for i in range(len(data)-1) )

def genData(self):
    """ Generates random data. """
    from random import randint
    return [randint(0,data_maximum) for i in range(data_length)]

def genPermutation(self):
    """ Generates a random permutation. """
    from random import shuffle
    x = range(data_length)
    shuffle(x)
    return x



# Testing functions

def testAlgorithm(self, number=100):
    """ Tests an algorithm with a number of random inputs. """
    for i in range(number):
        data = genData()
        data = algorithm()
        if not isSorted(data):
            print "Error! A counterexample was found!"
            print self.data
            return False
        print "The algorithm passed all tests"
        return True

def plotAlgorithm():
    pass



# Algorithm functions

def start():
    """ Starts the sorting process. """
    pass
