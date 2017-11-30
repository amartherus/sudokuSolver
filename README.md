# sudokuSolver

takes a text file in the format of the "sudokuProblem.txt" file in this repo. (9x9, empty squares represented by an underscore).

Solves all solvable sudoku problems using a modified backtracking algorithm.
(For those who are unfamiliar) the backtracking algorithm will essentially just take a guess at a given square on the board 
and continue solving. As soon as it runs into a contraint satisfaction error, it backtracks a step and keeps going. 
Basically its a depth first search for a solution.

My modification to the backtracking algorithm is that I first try to solve it using normal human methods.
I fill in all squares that only have one possible value remaining. I continue checking for this until I iterate through
the whole board without modifying it. This function alone can solve easy and medium sudoku problems.
If the game iterates the board without modifying, it kicks out and uses the backtracking algorithm to finish it out.

A brute force depth first search could take years to finish. 
By attempting to solve the puzzle using constraint satisfaction first, I significantly reduce the solve time. 
I believe it took my computer about 90ms to solve the sudokuProblem.txt problem.
