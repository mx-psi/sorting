# insertionSort.py

'''
Algorithmic efficiency:
Time:
  Average case: O(n**2)
  Worst case:   O(n**2)
  Best case:    O(n)
Auxiliary Space:
  Worst case:   O(1)
'''


import sorting

def insertion():
    """ Insertion Sort """
    data = sorting.start()
    
    for i in range(1,len(data)):
        sorting.iteration()
        
        # Picks an element and inserts it
        element = data[i]
        for j in reversed(range(i)):
            if data[j] > element:
                sorting.swap(j,j+1)
            else:
                data[j+1] = element
                break
            
    sorting.end()
    return data
