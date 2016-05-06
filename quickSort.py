# quickSort.py
# Use this as `plot.py quickSort.quick`

'''
Algorithmic efficiency:
Time:
  Average case: O(n*log(n))
  Worst case:   O(n**2)
  Best case:    O(n*log(n))
Auxiliary Space:
  Worst case:   O(n)
'''


import sorting

def quick():
    """ Quick sort """
    data = sorting.start()
    quicksort(data, 0, len(data) - 1)
    sorting.end()

    return data

def quicksort(data, lo, hi):
    """ Quick sort algorithm. Ported from https://github.com/fdavidcl/algoritmia/blob/master/quicksort.rb """
    pivot = data[lo]
    i, j = lo, hi

    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1

        if i <= j:
            sorting.iteration()
            sorting.swap(i, j)
            i += 1
            j -= 1

    if j > lo:
        quicksort(data, lo, j)
    if i < hi:
        quicksort(data, i, hi)
