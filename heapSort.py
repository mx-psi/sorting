# heapSort.py

'''
Algorithmic efficiency:
Time:
  Average case: O(n*log(n))
  Worst case:   O(n*log(n))
  Best case:    O(n*log(n))
Auxiliary Space:
  Worst case:   O(1)
'''

import sorting

def heapsort():
    """ Heap Sort. """
    global data
    data = sorting.start()
    
    # Converts into a heap
    global size
    size = len(data)
    for i in range(size/2, -1, -1):
        sorting.iteration()
        parent_child_exchange(i)

    # Flattens heap
    total_size = size
    for i in range(total_size-1,0,-1):
        sorting.iteration()
        sorting.swap(0,i)
        size -= 1
        parent_child_exchange(0)

    sorting.end()
    return data


def parent_child_exchange (i):
    left = 2*i+1
    right = 2*i+2
    change = 0
    
    if left >= size: return False
    if right >= size or data[left] > data[right]:
        change = left
    else:
        change = right
    
    if data[i] < data[change]:
        sorting.swap(i,change)
        parent_child_exchange(change)
    
    return True

