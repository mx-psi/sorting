#plot.py
#This file manages the plotting of the algorithm. 'plot.py -h' for usage.

from optparse import OptionParser
import sorting
import plotting



# Parser initialization and parsing

extra_help = """The algorithm should be provided as a function inside a Python module.
If the algorithm is the function 'heap' inside 'heapSort.py' you should call the program as follows:'plot.py [options] heapSort.heap'"""
parser = OptionParser(usage="usage: %prog [options] algorithm", epilog=extra_help)

parser.add_option("-s", "--swaps", action="store_true", default=False, help="Plots swaps")
parser.add_option("-b", "--bars", action="store_true", default=False, help="Plots bars instead of points")
parser.add_option("-l", "--length", type="int", default=80, help="Sets data lenght to LENGTH [default: %default]")

options, args = parser.parse_args()



# Configuration

if len(args) != 1 or not "." in args[0]: parser.error("Algorithm incorrectly provided.")
mod_name, alg_name = args[0].split(".")

sorting.algorithm = getattr(__import__(mod_name), alg_name)
sorting.plot_swaps = options.swaps
sorting.data_length = options.length
plotting.bars = options.bars

sorting.testAlgorithm()
sorting.plotAlgorithm()