import sorting

def bubbleSort(data):
    """ Bubble Sort algorithm. """
    
    plotting = sorting.Plotter(data)
    plotting.snapshot()

    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True

        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                is_sorted = False
        i = i+1

        plotting.snapshot()
    plotting.end()
    return data
