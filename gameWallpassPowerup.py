from gameTile import Tile
from gameBoard import board, boardRows, boardCols


class wallpassPowerup(Tile):
    def __init__(self, coordinates):
        # Initialises a wallpassPowerup
        # INHERITS from Tile class
        Tile.__init__(self, coordinates)
        self.descriptor = "wallpass"
        # ENCAPSULATES symbol so its not accessible as an attribute of the instance
        self._symbol = [['W', 'A', 'L', 'L'], ['P', 'A', 'S', 'S']]
        self.powerupCreated = True
        self.counter = '8'
        self.movesLeft = '0'
        self.showPowerup()

    def createTile(self):
        tile = [['W', 'A', 'L', 'L'], ['P', 'A', 'S', 'S']]
        return tile

    def showPowerup(self):
        # Shows the powerup with timer updating every frame
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [['W', 'A', self.counter, self.counter],
                                      ['L', 'L', self.counter, self.counter]]
        board.setBoardArray(boardArray)

    def destroyPowerup(self):
        # Destroys the powerup
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [[' ' for x in range(4)]
                                      for y in range(2)]
        board.setBoardArray(boardArray)
