# selectionSort.py

import sorting

def selection():
    """ Selection sort """
    data = sorting.start()

    n = len(data)
    for i in range(n-1):
        # Finds the minimum value
        minimum = data[i]
        min_pos = i
        for j in range(i+1,n):
            if data[j]<minimum:
                minimum = data[j]
                min_pos = j
        sorting.swap(min_pos,i)
        sorting.iteration()
    sorting.end()
    
    return data
