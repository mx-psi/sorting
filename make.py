##
# Sorting algorithms visualized.
#
# This code uses python2, matplotlib and avconv. You may need to install them.
#
# The idea was taken from "The Glowing Python":
#    http://glowingpython.blogspot.com.es/2013/02/selection-sort-animated.html
##

# make.py
# This file contains an example of use.
# It will create an animation of the algorithm in sorting.algorithm.

import sorting
import heapSort

sorting.algorithm = heapSort.heapsort
sorting.testAlgorithm()
sorting.plotAlgorithm()

