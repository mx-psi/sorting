# bubbleSort.py

import sorting


def bubble():
    """ Bubble Sort algorithm. """
    data = sorting.start()

    # Elements after last swap are already sorted.
    n = len(data)-1
    while n != 0:
        last_swap = 0
        for i in range(n):
            if data[i] > data[i+1]:
                sorting.swap(i,i+1)
                last_swap = i
        n = last_swap
        
        sorting.iteration()
    sorting.end()

    return data



