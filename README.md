Sorting
=======

Sorting is a plotter of sorting algorithms. It creates a video representing the changes an algorithm makes to a set of data. It uses [*python2*][1], [*matplotlib*][2] and [*avconv*][3] or [ffmpeg][4]. The original concept was taken from [The Glowing Python][5].

###Usage

####Algorithm
The sorting algorithm should be provided as a function inside a Python module, adding the functions provided in `sorting.py`.

The functions that should be included in the algorithm for its plotting are:

 - `sorting.start()`: Returns a list with a random permutation.
 - `sorting.swap(i,j)`: Swaps the contents of `data[i]` and `data[j]`.
 - `sorting.iteration()`: Plots current iteration.
 - `sorting.end()`: Finishes plotting and starts doing the video.

####Calling the program
Sorting uses Python's [`optparser`][6] module for parsing options. It includes various options such as plotting swaps, two different ways of plotting the algorithm and adjustment of data size and frame rate. You may call  `plot.py -h` for usage and information about options.


  [1]: https://www.python.org/download/releases/2.7.8/
  [2]: http://matplotlib.org
  [3]: https://libav.org/download.html
  [4]: https://ffmpeg.org
  [5]: http://glowingpython.blogspot.com.es/2013/02/selection-sort-animated.html
  [6]: https://docs.python.org/2/library/optparse.html
