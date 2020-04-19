# Search-Algorithms
This is a programming assignment done for the CSCI 561 - Aritifical Intelligence class.

The code in search.py implements the following search algorithm:
1) Breadth First Search
2) Uniform Cost Search
3) A* Search

#### Project description
In this project, we twist the problem of path planning a little bit just to give you the opportunity
to deepen your understanding of search algorithms by modifying search techniques to fit the
criteria of a realistic problem. To give you a realistic context for expanding your ideas about
search algorithms, we invite you to take part in a Mars exploration mission. The goal of this
mission is to send a sophisticated mobile lab to Mars to study the surface of the planet more
closely. We are invited to develop an algorithm to find the optimal path for navigation of the
rover based on a particular objective.

The input of our program includes a topographical map of the mission site, plus some
information about intended landing site and target locations and some other quantities that
control the quality of the solution. The surface of the planet can be imagined as a surface in a 3-
dimensional space. A popular way to represent a surface in 3D space is using a mesh-grid with a
Z value assigned to each cell that identifies the elevation of the planet at the location of the
cell. At each cell, the rover can move to each of 8 possible neighbor cells: North, North-East,
East, South-East, South, South-West, West, and North-West. Actions are assumed to be
deterministic and error-free (the rover will always end up at the intended neighbor cell).
The rover is not designed to climb across steep hills and thus moving to a neighboring cell
which requires the rover to climb up or down a surface which is steeper than a particular
threshold value is not allowed. This maximum slope (expressed as a difference in Z elevation
between adjacent cells) will be given as an input along with the topographical map.


#### Input: 

The file input.txt in the current directory of your program will be formatted as follows:

First line: Instruction of which algorithm to use, as a string: BFS, UCS or A*

Second line: Two strictly positive 32-bit integers separated by one space character, for
“W H” the number of columns (width) and rows (height), in cells, of the map.

Third line: Two positive 32-bit integers separated by one space character, for
“X Y” the coordinates (in cells) of the landing site. 0 £ X £ W-1 and 0 £ Y £ H-1
(that is, we use 0-based indexing into the map; X increases when moving East and
Y increases when moving South; (0,0) is the North West corner of the map).

Fourth line: Positive 32-bit integer number for the maximum difference in elevation between
two adjacent cells which the rover can drive over.
The difference in Z between two adjacent cells must be smaller than or equal (£ )
to this value for the rover to be able to travel from one cell to the other.

Fifth line: Strictly positive 32-bit integer N, the number of target sites.

Next N lines: Two positive 32-bit integers separated by one space character, for
“X Y” the coordinates (in cells) of each target site. 0 £ X £ W-1 and 0 £ Y £ H-1
(that is, we again use 0-based indexing into the map).

Next H lines: W 32-bit integer numbers separated by any numbers of spaces for the elevation
(Z) values of each of the W cells in each row of the map.

For example:

A*

8 6

4 4

7

2

1 1

6 3

0 0 0 0 0 0 0 0

0 60 64 57 45 66 68 0

0 63 64 57 45 67 68 0

0 58 64 57 45 68 67 0

0 60 61 67 65 66 69 0

0 0 0 0 0 0 0 0



Output: 
The file output.txt which your program creates in the current directory should be
formatted as follows:

N lines: Report the paths in the same order as the targets were given in the input.txt file.
Write out one line per target. Each line should contain a sequence of X,Y pairs
of coordinates of cells visited by the rover to travel from the landing site to the
corresponding target site for that line. Only use a single comma and no space
to separate X,Y and a single space to separate successive X,Y entries.
If no solution was found (target site unreachable by rover from given landing
site), write a single word FAIL in the corresponding line.

For example, output.txt may contain:

4,4 3,4 2,3 2,2 1,1

4,4 5,4 6,3
