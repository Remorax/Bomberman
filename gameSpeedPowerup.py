from gameTile import Tile
from gameBoard import board, boardRows, boardCols


class speedPowerup(Tile):
    def __init__(self, coordinates):
        # Initialises a wallpassPowerup
        # INHERITS from Tile class
        Tile.__init__(self, coordinates)
        self.descriptor = "speed"
        # ENCAPSULATES symbol so its not accessible as an attribute of the instance
        self._symbol = [['>' for i in range(4)] for j in range(2)]
        self.powerupCreated = True
        self.counter = '8'
        self.movesLeft = '0'
        self.showPowerup()

    def createTile(self):
        tile = [['>' for x in range(4)] for y in range(2)]
        return tile

    def showPowerup(self):
        # Shows the powerup with timer updating every frame
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [['>' if x < 2 else self.counter
                                       for x in range(4)] for y in range(2)]
        board.setBoardArray(boardArray)

    def destroyPowerup(self):
        # Destroys the powerup
        boardArray = board.getBoardArray()
        xcoord = self.getXCoordinate()
        ycoord = self.getYCoordinate()
        boardArray[ycoord][xcoord] = [[' ' for x in range(4)]
                                      for y in range(2)]
        board.setBoardArray(boardArray)
