import sys
from csp import *

#read file function
def readFile():
    filename = sys.argv[1]

    file = open(filename, "r") #opens file with name of the argument
    board = [];

    for line in file:
        board.append(line)

    file.close()
    return board

def getGivenValues(csp, board):
    for i in range(0,9):
        for j in range (0,9):
            if board[i][j] != '_':
                csp.domains[chr(i+65)+str(j+1)] = {int(board[i][j])}

def solveBasic(csp):
    modded = True
    while modded == True:
        modded = False #if I modify the board in this iteration
        #iterate through board and remove values found in neighbors
        for i in cross('ABCDEFGHI', '123456789'):
            neighbors = csp.neighbors[i]
            for j in neighbors:
                if len(csp.domains[j]) == 1 and len(csp.domains[i]) != 1:
                    #will use to compare later
                    temp = csp.domains[i].copy()
                    #remove the neighbor's number from the location I'm checking
                    csp.domains[i] = csp.domains[i] - csp.domains[j]
                    #if we actually made a modification in the line above...
                    if temp != csp.domains[i]:
                        modded = True

def backtrackingSearch(csp, count):
    assignment = {}
    for i in csp.domains:
        if len(csp.domains[i]) == 1:
            valueStr = str(csp.domains[i])
            assignment.update({i: valueStr[5]})
    return backtrack(assignment, csp, count)

def backtrack(assignment, csp, count):
    if all(i in assignment for i in cross('ABCDEFGHI', '123456789')):
        return assignment
    var = getVar(csp, assignment)

    for i in csp.domains[var]:
        if isConsistent(i, var, assignment):
            assignment.update({var: i})
            result = backtrack(assignment, csp, count)
            if all(i in assignment for i in cross('ABCDEFGHI', '123456789')):
                return result
            else:
                assignment.pop(var)
    return False

def isConsistent(value, var, assignment):
    #check col
    for i in 'ABCDEFGHI':
        if i+var[1] in assignment:
            if assignment[i+str(var[1])] == value: #check if the value is equal that key
                return False
    #check row
    for i in '123456789':
        if var[0]+i in assignment:
            if assignment[var[0]+i] == value: #check if the value is equal that key
                return False
    #check box
    boxList = makeBoxList()
    for i in range(0,9):
        if var in boxList[i]: #find the box that 'var' is in
            for j in range(0,9):
                if boxList[i][j] in assignment:
                    if assignment[boxList[i][j]] == value:
                        return False
    return True



def getVar(csp, assignment):
    smallest = 10
    for i in csp.domains:
        if i not in assignment:
            if smallest > len(csp.domains[i]):
                smallest = len(csp.domains[i])
    for i in csp.domains:
        if i not in assignment:
            if smallest == len(csp.domains[i]):
                return i

def printSolution(csp):
    domains = csp.domains
    for i in range(1, 10):
        for j in range(1, 10):
            location = chr(i+64)+str(j)
            print csp.domains[location],
            if j == 9:
                print '\n'

def main():
    count = 0
    board = readFile()
    csp = CSP()
    getGivenValues(csp, board)

    #solve sudoku as far as possible through normal methods
    modded = solveBasic(csp)
    assignments = backtrackingSearch(csp, count)
    csp.domains = assignments
    printSolution(csp)

main()
