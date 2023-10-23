
rawstr = '653718294248569317917234658594382176872196435136475982789643521421957863365821749'
row = []
col = []
mat = []




def lstring(string: str, length: int, char: str):
    out = ''
    if length - len(string) < 0:
        return string
    for _ in range(length - len(string)):
        out += char
    return out + string

def fastfindsqrt_WIP(perfsqr: int) -> int:
    """
    Fast Find Square Root\n
    !!! Near-Positively not needed !!!\n 
    \- only is useful when a distribution of expected square roots is given\n
    A function to find the square root of a number knowing it is a square root\n
    * num - the number to be square rooted. - num must be >= 1
    """
    """
    DO THIS AFTER LEARNING PROBABILITY
    """
    if perfsqr == 1:
        return 1
    i = 0 
    j = 0
    prevnum = lambda : 2**i
    num = lambda : 2**(i + 1)
    while num*num != perfsqr:
        if num*num < perfsqr:
            pass # increment
        elif num*num > perfsqr:
            pass # decrement
        else: # found
            return num

def maketestintlist(sidesize: int = 9) -> list[list[int]]:
    return [i for i in range(sidesize**2)]


#NEW VER - added
def _makeintlist(rawstr: str, valuelength: int = 1) -> list[int]:
    """
    Make Integer List\n
    Take in a string and return a list containing all values in said list\n
    Parameters:
        * rawstr - string to be converted into list
        * valuelength - length of each value in rawstr, default = 1\n
    Additional Info:
        * string length must be a perfect square
    """
    if len(rawstr) != int(len(rawstr)**(0.5))**2: 
        raise Exception("String length %d is not a perfect square" % (len(rawstr)))
    out: list[int] = []
    for i in range(0, len(rawstr), valuelength):
        out.append(int(rawstr[i : i + valuelength]))
    return out


"""
The _make### functions return a list based on the row/column/section selected.
row[i] = the ith row of the sudoku puzzle 
    (top = 0 to bottom = 8)

col[i] = the ith column of the sudoku puzzle 
    (left = 0 to right = 8)

sec[i] = the ith section of the sudoku puzzle 
    (top left 3x3 section = 0, top right 3x3 section = 2, bottom left 3x3 section = 6, bottom right 3x3 section = 8)
"""
def _makerow(intlist: list[int]) -> list[list[str]]:
    """
    Make Row Matrix\n
    Take in a list of integers and return a list containing a list of rows\n
        * intlist - list of integers to be converted into list of rows
    """
    sidesize = int(len(intlist)**0.5)
    #return [intlist[i : i + sidesize] for i in range(0, len(intlist), sidesize)] #single line
    out: list = []
    for i in range(0, len(intlist), sidesize):
        out.append(intlist[i : i + sidesize])
    return out

def _makecol(intlist: list[int]) -> list[list[str]]:
    """
    Make Col Matrix\n
    Take in a list of integers and return a list containing a list of columns\n
        * intlist - list of integers to be converted into list of rows
    """
    sidesize = int(len(intlist)**0.5)
    #return [[intlist[j] for j in range(i, len(intlist), sidesize)] for i in range(sidesize)] #single line
    out: list = []
    for i in range(sidesize):
        tempout: list = []
        for j in range(i, len(intlist), sidesize):
            tempout.append(intlist[j])
        out.append(tempout)
    return out

def _makesec(intlist: list[int]) -> list[list[str]]:
    """
    Make Sec Matrix\n
    Take in a list of integers and return a list containing a list of sections.\n
        * intlist - list of integers to be converted into list of rows\n
    each section cooresponds to a rectangular group of numbers within the 
    board - currently only 9 3x3 sections are implemented. (unique section size has not yet been implmented)\n
    \- Example:\n
        [ 0 ] [ 1 ] [ 2 ]\n
        [ 3 ] [ 4 ] [ 5 ]\n
        [ 6 ] [ 7 ] [ 8 ]\n
    The numbers refer to the index location of that 3x3 group of numbers, with the sublist having the same indexing method.\n
    """
    sidesize = int(len(intlist)**0.5)
    #return [[intlist[i+((i//3)%3)*6] for i in range(sec*3, sec*3+9)] for sec in range(sidesize)] #single line
    seclist: list[list[int]] = [[] for _ in range(sidesize)]
    for i in range(len(intlist)):
        seclist[((i//9)//3)*3 + (i%9)//3].append(intlist[i])
    return seclist
    

"""
The show###list functions print a string showing the current sudoku puzzle based on a ### list.

"""
def showrowlist(row: list[list[str]]) -> str:
    outline = ''
    for i in range(len(row)): #get mat
        outline += '  '.join([str(row[i][j : j + 3]) for j in range(0, len(row), 3)]) + '\n'
        if not i%3 - 2:
            outline += '\n'
    print(outline)
    return outline

def showcollist(col: list[list[str]]) -> str:
    size = int(len(intlist)**0.5)
    outline = ''
    for col_i in range(size):
        line = ''
        for i in range(size//3):
            secline = '['
            for j in range(size//3):
                secline += str(col[j+i*3][col_i]) +', '
            line += secline[:-2] + ']  '
        outline += line + '\n'
        if col_i % 3 == 2:
            outline += '\n'
    print(outline)
    return outline
        
def showseclist(sec: list[list[str]]) -> str:
    #Commented below is for future implementation of non standard grid sizes
    # size = len(intlist)
    # sidesize = int(len(intlist)**0.5)
    outline = ''
    for secseg_i in range(0, 9, 3):
        for line_i in range(3):
            secline = ''
            for sec_i in range(3):
                secline += str(sec[sec_i + secseg_i][line_i*3: line_i*3 + 3]) + '  '
            outline += secline + '\n'
        outline += '\n'
    
    print(outline)
    return outline

def generatetilepossibilities(index: int) -> list[int]:
    """
    
    """
    rowelements = set(row[index//9])
    colelements = set(col[index%9])
    secelements = set(sec[((index//9)//3)*3 + (index%9)//3])
    
    default = set([i for i in range(1,10)])

    return list(default - rowelements - colelements - secelements)



testrawstr = "000000001020000000000000000000000000000000000000000000000000000000000000300000000"
#intlist = _makeintlist(rawstr)
#intlist = maketestintlist()
intlist = _makeintlist(testrawstr)

row = _makerow(intlist)
col = _makecol(intlist)
sec = _makesec(intlist)

showrowlist(row)
# showcollist(col)
# showseclist(sec)


print(generatetilepossibilities(0))



class section:
    index: int
    possibilities: list[int]

    def __init__(self, index: int, possibilities: list[int]) -> None:
        self.index = index
        self.possibilities = possibilities

def sumn():
    testlist = []
    for i in range(9):
        testlist.append(section(i, [x for x in range(i)]))

    for i in testlist:
        j: section = i
        print(j.index, j.possibilities)

