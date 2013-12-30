# sorting.py
# This file contains testing and auxiliary functions.


import plotting


# General variables
data = []
data_maximum = 80


# Auxiliary functions

def isSorted():
    """ Returns true if the data is sorted in increasing order. """
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def genData():
    """ Generates random data. """
    from random import randint
    return [randint(0,data_maximum) for i in range(data_length)]

def genPermutation():
    """ Generates a random permutation. """
    from random import shuffle
    x = range(data_length)
    shuffle(x)
    return x



# Testing and plotting functions

def testAlgorithm(number=100):
    """ Tests an algorithm with a number of random inputs. """
    global data
    global test
    
    test = True
    for i in range(number):
        data = genData()
        data = algorithm()
        if not isSorted():
            print "Error! A counterexample was found!"
            print self.data
            return False
    return True

def plotAlgorithm():
    global data
    global test
    
    test = False
    data = genPermutation()
    data = algorithm()
    



# Algorithm functions

def start():
    """ Starts the sorting process and returns the original data. """
    return data

def swap(i,j):
    """ Swaps the contents of data[i] and data[j]. """
    data[i],data[j] = data[j],data[i]
    if plot_swaps and not test: plotting.swaps(i,j)

def iteration():
    """ It is called when the most external loop finishes the current iteration. """
    if not test: plotting.snapshot()

def end():
    """ It is called when the sorting process finishes. """
    if not test:
        plotting.snapshot()
        plotting.createMovie()
        plotting.restart()
