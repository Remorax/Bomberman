import os
import math
import random

from lazyme.string import color_print

from gameWall import Wall
from gameTile import Tile
from gameBrick import Brick


class Board(object):

    def __init__(self, dimensions):
        # Initialise board variables
        global boardRows, boardCols
        ''' Dimensions are ENCAPSULATED so its' not directly accessible
        from the instance '''
        self._dimensions = dimensions
        self.unoccupiedPositions = []
        self.brickPositions = self.calculateBrickPositions()
        self.unoccupiedPositionsPowerup = []
        self.enemyOnBomb = False
        self.enemyOnBombInstance = False
        self.bombermanOnBomb = False
        self.bombermanOnBombInstance = False
        self.wallpass = False
        self.isTemporaryWall = False
        self.temporaryWall = ('', '')
        self.score = "00"
        self.livesLeft = "01"
        self.blastRadius = []
        self.enemies = [(boardRows - 2, boardCols - 2), (1, boardCols - 4),
                        (boardRows - 3, 1), (5, 5)]
        self.numberOfEnemies = len(self.enemies)
        self.bombermanPosition = (1, 1)

    def getBoardWidth(self):
        return self._dimensions[1]

    def getBoardHeight(self):
        return self._dimensions[0]

    def tileTypeDecider(self, x, y):
        # Decides whether the tile created should be a wall or a brick
        if(x == 0 or y == 0 or x == (self._width - 1) or y == (self._height - 1)):
            return Wall
        elif(x % 2 == 0 and y % 2 == 0):
            self.unoccupiedPositionsPowerup.append((x, y))
            return Wall
        elif((x, y) in self.brickPositions):
            return Brick
        self.unoccupiedPositions.append((x, y))
        self.unoccupiedPositionsPowerup.append((x, y))
        return Tile

    def calculateBrickPositions(self):
        # Randomly generate coordinates for brick placement
        global boardRows, boardCols
        retList = []
        retList.extend([(i, j) for j in list(range(1, boardRows - 1))
                        for i in range(boardRows) if i % 2 == 1])
        retList.extend([(i, j) for j in list(range(1, boardCols - 1)) if j % 2 ==
                        1 for i in range(1, boardCols - 1) if i % 2 == 0])
        excluded = [(boardRows - 2, boardCols - 2), (1, boardCols - 4),
                    (boardRows - 3, 1), (5, 5)] + [(1, 1)]
        retList = list(set(retList) - set(excluded))
        sample = []
        for i, line in enumerate(retList):
            if i < 10:
                sample.append(line)
            elif i >= 10 and random.random() < 10 / float(i + 1):
                replace = random.randint(0, len(sample) - 1)
                sample[replace] = line
        return sample

    def getBoardArray(self):
        return self._boardArray

    def setBoardArray(self, newBoardArray):
        self._boardArray = newBoardArray

    def createBoard(self):
        self._width = int(self.getBoardWidth() / 4)
        self._height = int(self.getBoardHeight() / 2)
        os.system('tput reset')
        ''' Uses POLYMORPHISM to create the tile based on the class returned
            and then append its tile representation to the boardArray '''
        boardArray = [[self.tileTypeDecider(x, y)((x, y)).tileRepresentation
                       for x in range(self._width)] for y in
                      range(self._height)]
        color_print("SCORE: " + self.score, color='yellow',  end='', bold=True)
        color_print("\t\t\t\t\t   LIVES: " + self.livesLeft, color='yellow',
                    bold=True)
        # Print the board for the first time
        for (i, row) in enumerate(boardArray):
            for (j, tile) in enumerate(row):
                if((j, i) in self.enemies):
                    symbol = "[xx]" if ((j + i) % 3 == 1) else "[>>]"\
                        if ((j + i) % 3 == 0) else "|xx|"
                    color_print(symbol, color='red', highlight='green',
                                end='', bold=True)
                elif((j, i) == self.bombermanPosition):
                    color_print("[^^]", color='blue', highlight='cyan', end='',
                                bold=True)
                else:
                    string = ''.join(tile[0])
                    if(string == '####'):
                        color_print('    ', color='gray', highlight='gray',
                                    end='')
                    elif(string == "%%%%"):
                        color_print('~~~~', color='red', highlight='yellow',
                                    end='')
                    elif(string == '    '):
                        color_print(string, color='black', highlight='black',
                                    end='')
                    else:
                        color_print(string, color='red', end='', bold=True)
            print("\n", end='')
            for (j, tile) in enumerate(row):
                if((j, i) in self.enemies):
                    symbol = " ][ " if ((j + i) % 3 == 1) else " // "\
                        if ((j + i) % 3 == 0) else "|][|"
                    color_print(symbol, color='red', highlight='green',
                                end='', bold=True)
                elif((j, i) == self.bombermanPosition):
                    color_print(" ][ ", color='blue', highlight='cyan',
                                end='', bold=True)
                else:
                    string = ''.join(tile[0])
                    if(string == '####'):
                        color_print('    ', color='gray', highlight='gray',
                                    end='', bold=True, underline=True)
                    elif(string == "%%%%"):
                        color_print('~~~~', color='red', highlight='yellow',
                                    end='', bold=True, underline=True)
                    elif(string == '    '):
                        color_print(string, color='black', highlight='black',
                                    end='', bold=True, underline=True)
                    else:
                        color_print(string, color='red', end='', bold=True)
            print("\n", end='')

        self._boardArray = boardArray


def getBoardDimensions():
    # Get board dimensions based on the terminal size
    rows, columns = os.popen('stty size', 'r').read().split()
    rows = int(rows)
    columns = int(columns)
    possibleBoardRows = (rows - 4)
    while (possibleBoardRows % 4 != 2):
        possibleBoardRows -= 1
    possibleBoardRows = math.floor(possibleBoardRows / 2)
    if(possibleBoardRows * 4 <= columns):
        possibleBoardCols = possibleBoardRows
    else:
        possibleBoardCols = math.floor(columns / 4)
        possibleBoardRows = possibleBoardCols

    return (possibleBoardRows, possibleBoardCols)


boardRows, boardCols = getBoardDimensions()
board = Board((boardRows * 2, boardCols * 4))
