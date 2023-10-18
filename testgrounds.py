
rawstr = '653718294248569317917234658594382176872196435136475982789643521421957863365821749'
row = []
col = []
mat = []


def rowtest():
    print('Rows:\n' + str(row))

def coltest():
    print('\nColumns:\n' + str(col))

def mattest():
    print('\nColumns:\n' + str(mat))



def lstring(string: str, length: int, char: str):
    out = ''
    if len(string) - length < 0:
        return string
    for i in range(len(string) - length):
        out += char
    return out + string

def maketestrawstr() -> str:
    out: str = ''
    for i in range(81):
        i += 1
        out += lstring(i, 2, ' ')
    return out





def makerow(rawstr: str) -> list[list[str]]:
    out: list = []
    for i in range(0, len(rawstr), int(len(rawstr)/9)): #get rows
        out.append([*rawstr[i : i + 9]])
    return out

def makecol(rawstr: str) -> list[list[str]]:
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





row = makerow(rawstr)
col = makecol(rawstr)
mat = makemat(row)

maketestrawstr()

#showsudoku(row)