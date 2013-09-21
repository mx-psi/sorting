# bubbleSort.py

import sorting

def bubble(data, plot=True):
    """ Bubble Sort algorithm. """
    plotting = sorting.Plotter(data, plot)
    plotting.snapshot()

    # Elements after last swap are already ordered.
    n = len(data)-1
    while n != 0:
        last_swap = 0
        for i in range(n):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
                last_swap = i
        n = last_swap
        
        plotting.snapshot()
    plotting.end()

    return data


##
# def bubble(data, plot=True):
#     """ Classic Bubble Sort algorithm. """
#     plotting = sorting.Plotter(data, plot)
#     plotting.snapshot()
#
#     is_sorted = False
#     n = len(data)-1
#
#     while not is_sorted:
#         is_sorted = True
#         for j in range(n):
#             if data[j] > data[j+1]:
#                 data[j],data[j+1] = data[j+1],data[j]
#                 is_sorted = False
#         n = n-1
#
#         plotting.snapshot()
#     plotting.end()
#
#     return data
##



