##
# Sorting algorithms visualized.
#
# This code uses python2 and ffmpeg. You may need to install them.
#
# The idea was taken from "The Glowing Python":
#    http://glowingpython.blogspot.com.es/2013/02/selection-sort-animated.html
##

import sorting
import bubbleSort

datos = sorting.genData()
bubbleSort.bubbleSort(datos)
