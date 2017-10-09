from gameTile import Tile
from gameBoard import board
from gameBomberman import bomberman


class Bomb(Tile):
    def __init__(self, coordinates, powerup):
        # Initialises a Bomb
        # INHERITS from Tile class
        Tile.__init__(self, coordinates)
        self.detonated = False
        self.doubleExplosion = powerup

    def startBombTimer(self, counter):
        # Updates the bomb timer
        boardArray = board.getBoardArray()
        x = self.getXCoordinate()
        y = self.getYCoordinate()
        boardArray[y][x] = [[counter for i in range(4)] for j in range(2)]
        board.setBoardArray(boardArray)
        return

    def showExplosion(self, x, y):
        # Shows the explosion when the bomb detonates
        if (x, y) in board.unoccupiedPositions or\
           (x, y) in board.brickPositions:
            boardArray = board.getBoardArray()
            isStrongEnemy = False
            for enemy in board.enemiesArray:
                if(enemy.descriptor == 'strongEnemy' and
                   ((x, y) == (enemy.getXCoordinate(),
                               enemy.getYCoordinate()))):
                    isStrongEnemy = True
            if(not isStrongEnemy):
                boardArray[y][x] = [['^' for i in range(4)] for j in range(2)]
            else:
                # Strong enemy becomes weak on explosion
                boardArray[y][x] = [['[', 'x', 'x', ']'], [' ', ']', '[', ' ']]
            board.setBoardArray(boardArray)
            if(x, y) in board.brickPositions:
                # Destroys if it is a brick
                board.brickPositions.remove((x, y))
                board.unoccupiedPositions.append((x, y))
                board.score = str(int(board.score) + 10)
            board.blastRadius.append((x, y))
            return True
        return False

    def detonate(self):
        # Called when bomb timer reaches 0
        boardArray = board.getBoardArray()
        x = self.getXCoordinate()
        y = self.getYCoordinate()
        if((x, y) == (bomberman.getXCoordinate(), bomberman.getYCoordinate())):
            boardArray[y][x] = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]
        else:
            boardArray[y][x] = [[' ' for i in range(4)] for j in range(2)]
        output1 = self.showExplosion(x - 1, y)
        output2 = self.showExplosion(x + 1, y)
        output3 = self.showExplosion(x, y - 1)
        output4 = self.showExplosion(x, y + 1)
        if(self.doubleExplosion):
            # If bomberman has explosion powerup
            if(output1):
                self.showExplosion(x - 2, y)
            if(output2):
                self.showExplosion(x + 2, y)
            if(output3):
                self.showExplosion(x, y - 2)
            if(output4):
                self.showExplosion(x, y + 2)
        board.blastRadius.append((x, y))
        return
