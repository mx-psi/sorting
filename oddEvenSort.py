# oddEvenSort.py

##
# The snapshots are made outside the loops for making videos shorter. 
#
# If you want a step-by-step video, place them inside the for loops
##

import sorting

def oddEven(data, plot = True):
    """ Odd-even sort. """
    plotting = sorting.Plotter(data, plot)
    plotting.snapshot()
    n = len(data) -1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, n, 2):
            #Compares each couple [even,odd]
            if data[i] > data[i+1]:
                #Swaps and sets is_sorted to False
                data[i],data[i+1] = data[i+1],data[i]
                is_sorted = False
        plotting.snapshot()
        for i in range(1, n, 2):
            #Compares each couple [odd,even]
            if data[i] > data[i+1]:
                #Swaps and sets is_sorted to False
                data[i],data[i+1] = data[i+1],data[i]
                is_sorted = False
        plotting.snapshot()
    plotting.end()
    return data
        
