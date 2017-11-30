#Source: http://norvig.com/sudoku.html
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def makeBoxList():
    boxList = []
    for rs in ('ABC', 'DEF', 'GHI'):
        for cs in ('123', '456', '789'):
            boxList.append(cross(rs, cs))
    return boxList

class CSP:

    def __init__ (self):
        #sets all variables (locations)
        self.variables = list(cross('ABCDEFGHI', '123456789'))

        #map <location, set{possible values}>
        self.domains = {i: {1, 2, 3, 4, 5, 6, 7, 8, 9} for i in cross('ABCDEFGHI', '123456789')}

        #setting all neighbors
        self.neighbors = {i: set() for i in cross('ABCDEFGHI', '123456789')}
        for i in range(0,9): #iterate rows
            for j in range(1,10): #iterate columns
                #i+65 gets ascii value
                self.neighbors[chr(i+65)+str(j)].update(cross(chr(i+65), '123456789'))
                self.neighbors[chr(i+65)+str(j)].update(cross('ABCDEFGHI', str(j)))
                boxList = makeBoxList() #list of all 9 boxes with their location values
                for k in range(0,9): #iterate boxes
                    if chr(i+65)+str(j) in boxList[k]: #if our location is in this box
                        self.neighbors[chr(i+65)+str(j)].update(l for l in boxList[k])
        #TODO a location is not its own neighbor
        for i in self.neighbors:
            self.neighbors[i].remove(i)


    #boolean function that returns true if all of a variable's neighbors are different
    def allDiff(self, variable):
        if len(self.domains[variable]) == 1:
            for i in range(1, 10):
                #if columns are same, return false
                if self.domains[variable[0]+str(i)] == self.domains[variable] and variable[0]+str(i) != variable:
                    return False
                #if rows are same, return false
                if self.domains[chr(i+64)+variable[1]] == self.domains[variable] and chr(i+64)+variable[1] != variable:
                    return False
            #if box is same, return false
            boxList = makeBoxList()
            for i in range(1,10):
                if variable in boxList[i-1]: #find the box that 'variable' is in
                    for j in range(1,10):
                        if self.domains[boxList[i][j]] == self.domains[variable]:
                            return False
            #if you made it this far, you deserve to return true
            return True
        return False
