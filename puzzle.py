"""



"""

BOARD_AREA = 81

class GroupLayer:
    rawstring: list[list[str]]

    def __init__(self, rawstring) -> None:
        self.rawstring = rawstring

    def __eq__(self, __value: object) -> bool:
        if type(__value) is GroupLayer:
            if self.rawstring == __value.rawstring:
                return True
            return False
        raise TypeError("Incorrect type compared to GroupLayer. Compared object type: " + str(type(__value)))
    
    

class GroupMap:
    groupmap: dict[str : GroupLayer]

    def __init__(self, *layers: GroupLayer) -> None:
        for i in range(len(layers)):
            self.groupmap[i] = layers[i]

    def __eq__(self, __value: object) -> bool:
        if type(__value) is GroupMap:
            for i in self.groupmap.values(): # very basic version - On^2
                if i not in __value.groupmap.values():
                    return False
            return True
        raise TypeError("Incorrect type compared to GroupMap. Compared object type: " + str(type(__value)))
    
    def squish(self, grouplayer1: GroupLayer, grouplayer2: GroupLayer) -> None:
        pass

    def getpossibilities(self, location: list[int], value: int) -> list[int]:
        pass

class Board:
    
    rawstring: str #remove? - change to intlist?
    mainboard: list[int]
    col: list[list[int]]
    row: list[list[int]]
    mat: list[list[int]]

    indexstack: list[int] # represents a stack of indecies to be evaluated on

    def _isperfectsquare(num: int) -> bool:
        return int(num**0.5)**2 == num


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
    The below 3 functions should return index locations of columns, rows, sections etc.
    instead of returning values at those sections.

    TODO create "tile" class to hold (intlist) index location and possibilities
        possibilities being a list of integers containing the possible values at that tile
    """
    
    def _makerow(intlist: list[int]) -> list[list[str]]:
        """
        Make Row Matrix\n
        Take in a list of integers and return a list containing a list of rows\n
            * intlist - list of integers to be converted into list of rows\n
        Additional Information
        \- len(intlist) must be equal to sidesize**2
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
        #return
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
        #return [[intlist[j] for j in range(i, len(intlist), sidesize)] for i in range(sidesize)] #single line - NOT WORKING
        seclist: list[list[int]] = [[] for _ in range(sidesize)]
        for i in range(len(intlist)):
            seclist[((i//9)//3)*3 + (i%9)//3].append(intlist[i])
        return seclist


    def generatetilepossibilities(self, index: int) -> list[int]:
        """
        
        """
        rowelements = set(self.row[index//9])
        colelements = set(self.col[index%9])
        secelements = set(self.sec[((index//9)//3)*3 + (index%9)//3])
        default = set([i for i in range(1,10)])
        return list(default - rowelements - colelements - secelements)

    def generateboardpossibilities(self) -> None:
        """
        
        """
        pass

    def __init__(self, rawstring: str) -> None:
        if not self._isperfectsquare(len(rawstring)):
            raise Exception('Board size not prefect square')
        self.rawstring = rawstring

        intlist = self._makeintlist(rawstring)

        self.row = self._makerow(intlist)
        self.col = self._makecol(intlist)
        self.sec = self._makesec(intlist)


    
    def __eq__(self, __value: object) -> bool:
        if type(__value) is Board:
            return self.rawstring == __value.rawstring
        
        
        raise TypeError("Incorrect type compared to GroupMap. Compared object type: " + str(type(__value)))

    def __contains__(self, item: object) -> bool:
        if type(item) is Board:
            for i in range(len(self.rawstring)):
                if self.rawstring[i] != item.rawstring[i] and self.rawstring[i] != '0' and item.rawstring[i] != '0':
                    return False
            return True
        raise Exception('incorrect item \"contained\" in board')
    



class Puzzle:
    board: Board
    groupmap: GroupMap
    

    def __init__(self, rawpuzzlestring: str | Board, groupmap: GroupMap = None) -> None:
        if type(rawpuzzlestring) is Board:
            self.board = rawpuzzlestring
        else:
            self.board = Board(rawpuzzlestring)
        self.groupmap = groupmap
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) is Puzzle:
            if self.groupmap == __value.groupmap and self.board == __value.board:
                return True
            return False
        raise TypeError("Incorrect type compared to GroupMap. Compared object type: " + str(type(__value)))

    def __contains__(self, __item: object) -> bool:
        if type(__item) is Puzzle:
            if self.groupmap == __item.groupmap:
                if __item.board in self.board:
                    return True
                return False
            raise Exception('GroupMap\'s do not match.')
        raise Exception('incorrect item \"contained\" in Puzzle')





cellgroupmap: list[list[str]] = [
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [6, 6, 6, 7, 7, 7, 8, 8, 8],
    [6, 6, 6, 7, 7, 7, 8, 8, 8],
    [6, 6, 6, 7, 7, 7, 8, 8, 8]
]
cellGroupLayer = GroupLayer(cellgroupmap)

rowgroupmap: list[list[str]] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7, 7, 7, 7, 7],
    [8, 8, 8, 8, 8, 8, 8, 8, 8]
]
rowGroupLayer = GroupLayer(rowgroupmap)

columngroupmap: list[list[str]] = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
]
columnGroupLayer = GroupLayer(columngroupmap)

groupMap = GroupMap(cellGroupLayer, rowGroupLayer, columnGroupLayer)


rawpuzzlestring: str = '050010200008500010000030008000002000070006030100070900700000500400000060300800040'
puzzleboard = Board(rawpuzzlestring)

sudokupuzzle = Puzzle(puzzleboard, groupMap)


rawsolvedpuzzlestring: str = '653718294248569317917234658594382176872196435136475982789643521421957863365821749'
solvedpuzzleboard = Board(rawsolvedpuzzlestring)

solvedsudokupuzzle = Puzzle(solvedpuzzleboard, groupMap)