
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

def maketestrawstr_outdated() -> list:
    out: list = []
    for i in range(81):
        out.append(lstring(str(i), 2, ' '))
    return out

def maketestintlist(sidesize: int = 9) -> list[list[int]]:
    return [i for i in range(sidesize**2)]



def showseclist_2_diffver(mat: list[list[str]]) -> str:
    size = int(len(intlist)**0.5)
    outline: str = ''
    for sec_i in range(9):
        outrow: str = ''
        for line_i in range(0, 9, 3):
            outrow += str(mat[sec_i][line_i: line_i + 3]) + ' '
        outline += '\n'
        if sec_i%3 == 2:
            outline += outrow + '\n'
    print(outline)
    return outline

def makerow_old(rawstr: str) -> list[list[str]]:
    """
    Make Row Matrix\n
    Take in a list of integers and return a list containing a list of rows\n
        * intlist - list of integers to be converted into list of rows
    """
    out: list = []
    for i in range(0, len(rawstr), int(len(rawstr)/9)): #get rows
        out.append([*rawstr[i : i + 9]])

    return out

def makecol_old(rawstr: str | list) -> list[list[str]]:
    out: list = []
    for i in range(9): #get columns
        out.append([rawstr[j] for j in range(i, len(rawstr), int(len(rawstr)/9)) ])
    return out

def makesec_old(row: list[list[str]]) -> list[list[str]]:
    out: list = []
    for i in range(9): #get mat
        pass
    return out


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
    



    # TODO FIX FIX FIXFIXFIXFIXFIXFIXFIXFIXFIX




    for segment in range(3):
        for line_i in range(3):
            seclist.extend([intlist[segment*3:(segment+1)*3]])

    """ ONLY WORKS FOR TEST LIST
    seclist: list[list[int]] = [[] for _ in range(sidesize)]
    for num in intlist:
        print(seclist)
        seclist[((num//9)//3)*3 + (num%9)//3].append(num)
    return seclist
    """





def showrowlist(row: list[list[str]]) -> str:
    outline = ''
    for i in range(len(row)): #get mat
        outline += '  '.join([str(row[i][j : j + 3]) for j in range(0, len(row), 3)]) + '\n'
        if not i%3 - 2:
            outline += '\n'
    print(outline)
    print(row)
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
        
def showseclist(mat: list[list[str]]) -> str:
    size = int(len(intlist)**0.5)
    outline = ''

    secarea = ''
    print(mat)
    for i in range(3):
        secarea += str(mat[0][i*3:(i*3)+3]) + ' '
    #print(secarea)

    """
    for i in range(3):
        for j in range(3):
            for line_i in range(3):
                secline = ''
                for sec_i in range(3):
                    secline += str(mat[line_i][sec_i*3: sec_i*3 + 3]) + '  '
            outline += secline + '\n'
        outline += '\n'
    """


    print(outline)
    return outline






intlist = _makeintlist(rawstr)
#intlist = maketestintlist()


row = _makerow(intlist)
col = _makecol(intlist)
sec = _makesec(intlist)

showrowlist(row)
#showcollist(col)
showseclist(sec)


# newintlist: list[int] = []
# for i in intlist:
#     newintlist.append(((i//9)//3)*3 + (i%9)//3)

# newrow = _makerow(newintlist)

# showrowlist(newrow)