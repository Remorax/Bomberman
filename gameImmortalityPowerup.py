from gameTile import Tile
from gameBoard import board, boardRows, boardCols


class immortalityPowerup(Tile):
    def __init__(self, coordinates):
        # Initialises a wallpassPowerup
        # INHERITS from Tile class
        Tile.__init__(self, coordinates)
        self.descriptor = "immortality"
        # ENCAPSULATES symbol so its not accessible as an attribute of the instance
        self._symbol = [['I', 'M', 'M', 'O'], ['R', 'T', 'A', 'L']]
        self.powerupCreated = True
        self.counter = '8'
        self.movesLeft = '0'
        self.showPowerup()

    def createTile(self):
        tile = [['I', 'M', 'M', 'O'], ['R', 'T', 'A', 'L']]
        return tile

    def showPowerup(self):
        # Shows the powerup with timer updating every frame
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [['I', 'M', self.counter, self.counter],
                                      ['M', 'O', self.counter, self.counter]]
        board.setBoardArray(boardArray)

    def destroyPowerup(self):
        # Destroys the powerup
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [[' ' for x in range(4)]
                                      for y in range(2)]
        board.setBoardArray(boardArray)
