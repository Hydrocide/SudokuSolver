
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


def fastfindsqrt(perfsqr: int) -> int:
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

def maketestrawstr() -> list:
    out: list = []
    for i in range(81):
        out.append(lstring(str(i), 2, ' '))
    return out

def maketestraw() -> list[list[int]]:
    out: list[list[int]]
    for i in range(9):
        tempout: list[int] = []
        for j in range(9):
            pass



#NEW VER
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

#NEW VER
def makerow(intlist: list[int], sidesize: int) -> list[list[str]]:
    """
    Make Row Matrix\n
    Take in a list of integers and return a list containing a list of rows\n
        * intlist - list of integers to be converted into list of rows\n
    Additional Information
    \- len(intlist) must be equal to sidesize**2
    """
    out: list = []
    for i in range(0, len(intlist), sidesize):
        out.append(intlist[i : i + sidesize])
    return out

def makerow_old(intlist: list[int]) -> list[list[str]]:
    """
    Make Row Matrix\n
    Take in a list of integers and return a list containing a list of rows\n
        * intlist - list of integers to be converted into list of rows
    """
    out: list = []
    for i in range(0, len(rawstr), int(len(rawstr)/9)): #get rows
        out.append([*rawstr[i : i + 9]])
    return out

def makecol(rawstr: str | list) -> list[list[str]]:
    out: list = []
    for i in range(9): #get columns
        out.append([rawstr[j] for j in range(i, len(rawstr), int(len(rawstr)/9)) ])
    return out

def makemat(row: list[list[str]]) -> list[list[str]]:
    out: list = []
    for i in range(9): #get mat
        pass
    return out



def showsudoku(row: list[list[str]]):
    outline: str =''
    for i in range(9): #get mat
        outline += '  '.join([str(row[i][j : j + 3]) for j in range(0, 9, 3)]) + '\n'
        if not i%3 - 2:
            outline += '\n'
    print(outline)


tl1 = []
for i in range(9):
    tl2 = []
    for j in range(9):
        tl2.append(i*9 + j)
    tl1.append(tl2)


row = makerow(rawstr)
col = makecol(rawstr)
mat = makemat(row)

rawtest = maketestrawstr()

testrow = makerow(rawtest)

#showsudoku(row)
#showsudoku(testrow)

