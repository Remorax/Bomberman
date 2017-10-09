from gameBoard import board


class Person():
    def __init__(self, xinit, yinit):
        ''' The coordinates and the symbol are ENCAPSULATED so it can't
        be directly accessed as an attribute of the instance'''
        self._x = xinit
        self._y = yinit
        self._xinit = xinit
        self._yinit = yinit
        self._symbol = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        self.speedPowerup = False

    def getXInit(self):
        return self._xinit

    def getYInit(self):
        return self._yinit

    def getXCoordinate(self):
        return self._x

    def getYCoordinate(self):
        return self._y

    def setXCoordinate(self, xnew):
        self._x = xnew
        return

    def setYCoordinate(self, ynew):
        self._y = ynew
        return

    def move(self, deltax, deltay):
        # Move the person given deltax and deltay
        xold = self.getXCoordinate()
        yold = self.getYCoordinate()
        activePowerup = False
        if ((xold + deltax, yold + deltay) not in board.unoccupiedPositions):
            if(abs(deltax) > 1 or abs(deltay) > 1):
                if(xold + int(deltax / 2), yold + int(deltay / 2))\
                        not in board.unoccupiedPositions:
                    return False
                else:
                    deltax = int(deltax / 2)
                    deltay = int(deltay / 2)
            else:
                if(not board.wallpass):
                    return False
                else:
                    if((xold + deltax, yold + deltay) not in
                       board.unoccupiedPositionsPowerup or
                       (not board.handleWallpassPowerup())):
                        return False
                    else:
                        activePowerup = True
        else:
            if(abs(deltax) > 1 or abs(deltay) > 1):
                if(xold + int(deltax / 2), yold + int(deltay / 2)) not in\
                        board.unoccupiedPositions:
                    if(not board.wallpass):
                        return False
                    else:
                        if((xold + int(deltax / 2), yold + int(deltay / 2))
                           not in board.unoccupiedPositionsPowerup)\
                                or (not board.handleWallpassPowerup()):
                            return False
        xnew = xold + deltax
        ynew = yold + deltay
        self.setXCoordinate(xnew)
        self.setYCoordinate(ynew)
        boardArray = board.getBoardArray()
        if(self._symbol == [['[', 'x', 'x', ']'], [' ', ']', '[', ' ']] or
           self._symbol == [['|', 'x', 'x', '|'], ['|', ']', '[', '|']] or
           self._symbol == [['[',  '>', '>', ']'], [' ', '/', '/', ' ']]):
            if(not board.enemyOnBomb):
                # Set the old position to an 'empty' tile
                boardArray[yold][xold] = [[' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ']]
            else:
                ''' Enemy is on the bomb. Show enemy, but also decrement
                bomb counter'''
                actualBomb = board.enemyOnBombInstance[0]
                actualBomb.startBombTimer(
                    str(board.enemyOnBombInstance[1] - 1)
                )
                board.enemyOnBomb = False
                board.enemyOnBombInstance = False
        else:
            if(not board.bombermanOnBomb):
                if(not board.isTemporaryWall):
                    # Set the old position to an 'empty' tile
                    boardArray[yold][xold] = [[' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ']]
                else:
                    boardArray[board.temporaryWall[1]][board.temporaryWall[0]]\
                        = [['#' for i in range(4)] for j in range(2)]
                    board.isTemporaryWall = False
            else:
                ''' Bomberman is on the bomb. Show bomberman, but also decrement
                bomb counter'''
                actualBomb = board.bombermanOnBombInstance[0]
                actualBomb.startBombTimer(
                    str(board.bombermanOnBombInstance[1] -
                        1)
                )
                board.bombermanOnBomb = False
                board.bombermanOnBombInstance = False

        ''' Decide whether enemy or bomberman is on the bomb by iterating
            through the list of active bombs '''
        for activeBomb in self.activeBombs:
            bombInstance = activeBomb[0]
            if((xnew, ynew) == (bombInstance.getXCoordinate(),
                                bombInstance.getYCoordinate())):
                if(self._symbol == [['[', 'x', 'x', ']'],
                                    [' ', ']', '[', ' ']] or
                   self._symbol == [['|', 'x', 'x', '|'],
                                    ['|', ']', '[', '|']] or
                   self._symbol == [['[',  '>', '>', ']'],
                                    [' ', '/', '/', ' ']]):
                    board.enemyOnBomb = True
                    board.enemyOnBombInstance = activeBomb
                elif(self._symbol == [['[', '^', '^', ']'],
                                      [' ', ']', '[', ' ']]):
                    board.bombermanOnBomb = True
                    board.bombermanOnBombInstance = activeBomb
                break
        # Set the new position accordingly
        boardArray[ynew][xnew] = self._symbol
        board.setBoardArray(boardArray)
        if(activePowerup):
            board.isTemporaryWall = True
            board.temporaryWall = (xnew, ynew)
        return True
