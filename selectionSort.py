# selectionSort.py

'''
Algorithmic efficiency:
Time:
  Average case: O(n**2)
  Worst case:   O(n**2)
  Best case:    O(n**2)
Auxiliary Space:
  Worst case:   O(1)
'''


import sorting

def selection():
    """ Selection sort """
    data = sorting.start()

    n = len(data)
    for i in range(n-1):
        sorting.iteration()
        # Finds the minimum value
        minimum = data[i]
        min_pos = i
        for j in range(i+1,n):
            if data[j]<minimum:
                minimum = data[j]
                min_pos = j
        sorting.swap(min_pos,i)
    sorting.end()
    
    return data
