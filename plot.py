# plot.py

##
# Sorting algorithms visualized.
#
# This code uses python2, matplotlib and avconv. You may need to install them.
#
# The idea was taken from "The Glowing Python":
#    http://glowingpython.blogspot.com.es/2013/02/selection-sort-animated.html
##

# This file manages the plotting of the algorithm. 'plot.py -h' for usage.

from optparse import OptionParser
import sorting
import plotting



# Parser initialization and parsing

extra_help = """Sorting uses matplotlib and avconv. You may need to install them.
The algorithm should be provided as a function inside a Python module.
If the algorithm is the function 'heapsort' inside 'heapSort.py' you should call the program as follows:'plot.py [options] heapSort.heapsort'.
See http://github.com/M42/sorting for more information."""

parser = OptionParser(usage="usage: %prog [options] algorithm", epilog=extra_help)

parser.add_option("-s", "--swaps", action="store_true", default=False, help="plot swaps")
parser.add_option("-b", "--bars", action="store_true", default=False, help="plot bars instead of points")
parser.add_option("-l", "--length", type="int", default=80, help="set data lenght[default: %default]")
parser.add_option("-r", "--rate", type="int", default=20, help="set frame rate (Hz value, fraction or abbreviation) [default: %default]")


options, args = parser.parse_args()



# Configuration

if len(args) != 1 or not "." in args[0]: parser.error("Algorithm incorrectly provided.")
mod_name, alg_name = args[0].split(".")

sorting.algorithm = getattr(__import__(mod_name), alg_name)
sorting.plot_swaps = options.swaps
sorting.data_length = options.length
plotting.bars = options.bars
plotting.rate = options.rate

# Start of the plot

sorting.testAlgorithm()
sorting.plotAlgorithm()
