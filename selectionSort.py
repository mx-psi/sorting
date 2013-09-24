# selectionSort.py

import sorting

def selection(data, plot=True):
    """ Selection sort """
    plotting = sorting.Plotter(data, plot)
    plotting.snapshot()

    n = len(data)
    for i in range(n-1):
        # Finds the minimum value
        minimum = data[i]
        min_pos = i
        for j in range(i+1,n):
            if data[j]<minimum:
                minimum = data[j]
                min_pos = j        
        # Swaps values
        data[min_pos],data[i] = data[i],minimum

        plotting.snapshot()
    plotting.end()
    return data
