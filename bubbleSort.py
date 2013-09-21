# bubbleSort.py

import sorting

def bubbleSort(data, plot=True):
    """ Bubble Sort algorithm. """
    
    plotting = sorting.Plotter(data, plot)
    plotting.snapshot()

    is_sorted = False
    n = len(data)-1

    while not is_sorted:
        is_sorted = True

        for j in range(n):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                is_sorted = False
        n = n-1

        plotting.snapshot()
    plotting.end()
    return data
