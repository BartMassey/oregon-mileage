# Oregon Mileage Data
Bart Massey  2014-08-20

This data originally came from the Oregon Department of
Transportation (ODOT). It is effectively a weighted
undirected graph in edge-list format, where each edge is the
mileage between two Oregon cities.

There are two graphs:

* The file `oregon-mileage.txt` contains the original ODOT
  map, with some gross triangle-inequality errors removed.
  All remaining triangle-inequality errors are less than
  10 miles.

* The file `oregon-mileage-map.txt` contains just the edges
  that cannot be removed from the original data without
  losing information.  This was produced by the Python
  program `reduce-mileages.py` in the distribution.

The data is, as far as I know, in the public domain. The
software is made available under the MIT License. Please
see the file COPYING in this distribution for license terms.
