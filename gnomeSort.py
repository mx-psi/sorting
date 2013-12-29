# gnomeSort.py

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

def gnome():
    """Gnome Sort algorithm. Also known as Stupid Sort."""
    data = sorting.start()
    i = 1
    while i < len(data):
        if data[i] >= data[i-1]: 
            #Pair is ordered. Check the next one.
            i += 1
        else:
            #Pair isn't ordered. Swap it and check the pair below.
            sorting.iteration()
            sorting.swap(i,i-1)
            if i > 1: i-=1
    sorting.end()
    return data