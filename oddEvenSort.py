# oddEvenSort.py

import sorting

def oddEven(data, plot = True):
    """ Odd-even sort. """
    data = sorting.start()
    n = len(data) -1
    is_sorted = False
    a = 0
    while not is_sorted:
        
        is_sorted = True
        
        for i in range(a, n, 2):
            if data[i] > data[i+1]:
                sorting.swap(i,i+1)
                is_sorted = False
                
        a = not a 
        sorting.iteration()
        
    sorting.end()
    return data
        
