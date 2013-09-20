import sorting

def bubbleSort(data):
    """ Bubble Sort algorithm. """
    
    plotting = sorting.Plotter(data)
    plotting.snapshot()

    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

        plotting.snapshot()
    plotting.end()
    
    return data
