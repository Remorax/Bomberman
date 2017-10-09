from gameTile import Tile
from gameBoard import board, boardRows, boardCols


class explosionPowerup(Tile):
    def __init__(self, coordinates):
        # Initialises a wallpassPowerup
        # INHERITS from Tile class
        Tile.__init__(self, coordinates)
        self.descriptor = "explosion"
        # ENCAPSULATES symbol so its not accessible as an attribute of the instance
        self._symbol = [['B', 'O', 'O', 'M'], ['B', 'O', 'O', 'M']]
        self.powerupCreated = True
        self.counter = '5'
        self.movesLeft = '0'
        self.showPowerup()

    def createTile(self):
        tile = [['B', 'O', 'O', 'M'], ['B', 'O', 'O', 'M']]
        return tile

    def showPowerup(self):
        # Shows the powerup with timer updating every frame
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [['B', 'O', self.counter, self.counter],
                                      ['O', 'M', self.counter, self.counter]]
        board.setBoardArray(boardArray)

    def destroyPowerup(self):
        # Destroys the powerup
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [[' ' for x in range(4)]
                                      for y in range(2)]
        board.setBoardArray(boardArray)
