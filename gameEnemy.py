from gamePerson import Person
from random import randint
from gameBoard import board, boardRows, boardCols


class Enemy(Person):

    def __init__(self, xinit, yinit):
        # INHERITS from Person class
        Person.__init__(self, xinit, yinit)
        ''' The symbol is ENCAPSULATED so it can't be directly accessed
        as an attribute of the instance'''
        self._symbol = [['[', 'x', 'x', ']'], [' ', ']', '[', ' ']]
        self.numberOfLives = 1
        self.descriptor = "enemy"
        self.activeBombs = []

    def getPseudoRandomInteger(self):
        ''' Generate pseudo random change in x and change in y for enemy movement
        based on whether the tile is unoccupied or not '''
        xold = self.getXCoordinate()
        yold = self.getYCoordinate()
        rand = randint(0, 1)
        if(xold == (boardCols - 2) and yold == (boardRows - 2)):
            if((xold, yold - 1) not in board.brickPositions and
               (xold - 1, yold) not in board.brickPositions):
                return (0, -1) if(rand == 0) else (-1, 0)
            elif((xold, yold - 1) in board.brickPositions and
                 (xold - 1, yold) in board.brickPositions):
                return (0, 0)
            elif((xold, yold - 1) in board.brickPositions):
                return (-1, 0)
            else:
                return (0, -1)
        elif(xold == 1 and yold == 1):
            if((xold, yold + 1) not in board.brickPositions and
               (xold + 1, yold) not in board.brickPositions):
                return (0, 1) if(rand == 0) else (1, 0)
            elif((xold, yold + 1) in board.brickPositions and
                 (xold + 1, yold) in board.brickPositions):
                return (0, 0)
            elif((xold, yold + 1) not in board.brickPositions):
                return (0, 1)
            else:
                return (1, 0)
        elif(xold == (boardCols - 2)):
            if(yold % 2 == 0):
                if((xold, yold + 1) not in board.brickPositions and
                   (xold, yold - 1) not in board.brickPositions):
                    return (0, 1) if(rand == 0) else (0, -1)
                elif((xold, yold + 1) in board.brickPositions and
                     (xold, yold - 1) in board.brickPositions):
                    return (0, 0)
                elif((xold, yold + 1) not in board.brickPositions):
                    return (0, 1)
                else:
                    return (0, -1)
            else:
                if(yold == 1):
                    if((xold, yold + 1) not in board.brickPositions and
                       (xold - 1, yold) not in board.brickPositions):
                        return (0, 1) if(rand == 0) else (-1, 0)
                    elif((xold, yold + 1) in board.brickPositions and
                         (xold - 1, yold) in board.brickPositions):
                        return (0, 0)
                    elif((xold, yold + 1) not in board.brickPositions):
                        return (0, 1)
                    else:
                        return (-1, 0)
                else:
                    a = randint(0, 1)
                    if(a == 0):
                        if((xold - 1, yold) not in board.brickPositions):
                            return(-1, 0)
                        return (0, 0)
                    else:
                        if((xold, yold + 1) not in board.brickPositions and
                           (xold, yold - 1) not in board.brickPositions):
                            return (0, 1) if(rand == 0) else (0, -1)
                        elif((xold, yold + 1) in board.brickPositions and
                             (xold, yold - 1) in board.brickPositions):
                            return (0, 0)
                        elif((xold, yold + 1) not in board.brickPositions):
                            return (0, 1)
                        else:
                            return (0, -1)
        elif(yold == (boardRows - 2)):
            if(xold % 2 == 0):
                if((xold + 1, yold) not in board.brickPositions and
                   (xold - 1, yold) not in board.brickPositions):
                    return (1, 0) if(rand == 0) else (-1, 0)
                elif((xold + 1, yold) in board.brickPositions and
                     (xold - 1, yold) in board.brickPositions):
                    return (0, 0)
                elif((xold + 1, yold) not in board.brickPositions):
                    return (1, 0)
                else:
                    return (-1, 0)
            else:
                if(xold == 1):
                    if((xold + 1, yold) not in board.brickPositions and
                       (xold, yold - 1) not in board.brickPositions):
                        return (1, 0) if(rand == 0) else (0, -1)
                    elif((xold + 1, yold) in board.brickPositions and
                         (xold, yold - 1) in board.brickPositions):
                        return (0, 0)
                    elif((xold + 1, yold) not in board.brickPositions):
                        return (1, 0)
                    else:
                        return (0, -1)
                else:
                    a = randint(0, 1)
                    if(a == 0):
                        if((xold, yold - 1) not in board.brickPositions):
                            return(0, -1)
                        return (0, 0)
                    else:
                        if((xold + 1, yold) not in board.brickPositions and
                           (xold - 1, yold) not in board.brickPositions):
                            return (1, 0) if(rand == 0) else (-1, 0)
                        elif((xold + 1, yold) in board.brickPositions and
                             (xold - 1, yold) in board.brickPositions):
                            return (0, 0)
                        elif((xold + 1, yold) not in board.brickPositions):
                            return (1, 0)
                        else:
                            return (-1, 0)
        elif(xold == 1):
            if(yold % 2 == 0):
                if((xold, yold + 1) not in board.brickPositions and
                   (xold, yold - 1) not in board.brickPositions):
                    return (0, 1) if(rand == 0) else (0, -1)
                elif((xold, yold + 1) in board.brickPositions and
                     (xold, yold - 1) in board.brickPositions):
                    return (0, 0)
                elif((xold, yold + 1) not in board.brickPositions):
                    return (0, 1)
                else:
                    return (0, -1)
            else:
                if(yold == 1):
                    if((xold, yold + 1) not in board.brickPositions and
                       (xold - 1, yold) not in board.brickPositions):
                        return (0, 1) if(rand == 0) else (-1, 0)
                    elif((xold, yold + 1) in board.brickPositions and
                         (xold - 1, yold) in board.brickPositions):
                        return (0, 0)
                    elif((xold, yold + 1) not in board.brickPositions):
                        return (0, 1)
                    else:
                        return (-1, 0)
                else:
                    a = randint(0, 1)
                    if(a == 0):
                        if((xold + 1, yold) not in board.brickPositions):
                            return(1, 0)
                        return (0, 0)
                    else:
                        if((xold, yold + 1) not in board.brickPositions and
                           (xold, yold - 1) not in board.brickPositions):
                            return (0, 1) if(rand == 0) else (0, -1)
                        elif((xold, yold + 1) in board.brickPositions and
                             (xold, yold - 1) in board.brickPositions):
                            return (0, 0)
                        elif((xold, yold + 1) not in board.brickPositions):
                            return (0, 1)
                        else:
                            return (0, -1)
        elif(yold == 1):
            if(xold % 2 == 0):
                if((xold + 1, yold) not in board.brickPositions and
                   (xold - 1, yold) not in board.brickPositions):
                    return (1, 0) if(rand == 0) else (-1, 0)
                elif((xold + 1, yold) in board.brickPositions and
                     (xold - 1, yold) in board.brickPositions):
                    return (0, 0)
                elif((xold + 1, yold) not in board.brickPositions):
                    return (1, 0)
                else:
                    return (-1, 0)
            else:
                if(xold == 1):
                    if((xold + 1, yold) not in board.brickPositions and
                       (xold, yold + 1) not in board.brickPositions):
                        return (1, 0) if(rand == 0) else (0, 1)
                    elif((xold + 1, yold) in board.brickPositions and
                         (xold, yold + 1) in board.brickPositions):
                        return (0, 0)
                    elif((xold + 1, yold) not in board.brickPositions):
                        return (1, 0)
                    else:
                        return (0, 1)
                else:
                    a = randint(0, 1)
                    if(a == 0):
                        if((xold, yold + 1) not in board.brickPositions):
                            return(0, 1)
                        return (0, 0)
                    else:
                        if((xold + 1, yold) not in board.brickPositions and
                           (xold - 1, yold) not in board.brickPositions):
                            return (1, 0) if(rand == 0) else (-1, 0)
                        elif((xold + 1, yold) in board.brickPositions and
                             (xold - 1, yold) in board.brickPositions):
                            return (0, 0)
                        elif((xold + 1, yold) not in board.brickPositions):
                            return (1, 0)
                        else:
                            return (-1, 0)
        else:
            if(xold % 2 == 0 and yold % 2 != 0):
                if((xold + 1, yold) not in board.brickPositions and
                   (xold - 1, yold) not in board.brickPositions):
                    return (1, 0) if(rand == 0) else (-1, 0)
                elif((xold + 1, yold) in board.brickPositions and
                     (xold - 1, yold) in board.brickPositions):
                    return (0, 0)
                elif((xold + 1, yold) not in board.brickPositions):
                    return (1, 0)
                else:
                    return (-1, 0)
            elif(xold % 2 != 0 and yold % 2 == 0):
                if((xold, yold + 1) not in board.brickPositions and
                   (xold, yold - 1) not in board.brickPositions):
                    return (0, 1) if(rand == 0) else (0, -1)
                elif((xold, yold + 1) in board.brickPositions and
                     (xold, yold - 1) in board.brickPositions):
                    return (0, 0)
                elif((xold, yold + 1) not in board.brickPositions):
                    return (0, 1)
                else:
                    return (0, -1)
            else:
                a = randint(0, 1)
                b = randint(0, 1)
                if(a == 0):
                    if(b == 0):
                        if((xold - 1, yold) not in board.brickPositions):
                            return(-1, 0)
                        return (0, 0)
                    else:
                        if((xold + 1, yold) not in board.brickPositions):
                            return(1, 0)
                        return (0, 0)
                else:
                    if(b == 0):
                        if((xold, yold - 1) not in board.brickPositions):
                            return(0, -1)
                        return (0, 0)
                    else:
                        if((xold, yold + 1) not in board.brickPositions):
                            return(0, 1)
                        return (0, 0)

    def destroyEnemy(self):
        # Kills the enemy by removing it from the list of enemies
        self.numberOfLives -= 1
        if(self.numberOfLives <= 0):
            xcoord = self.getXInit()
            ycoord = self.getYInit()
            try:
                board.enemies.remove((xcoord, ycoord))
            except:
                pass
            for enemy in board.enemiesArray:
                if((enemy.getXInit(), enemy.getYInit()) == (xcoord, ycoord)):
                    board.enemiesArray.remove(enemy)
                    break
            board.numberOfEnemies -= 1
        else:
            # Enemy is powerful, 2 explosions to die
            # Strong enemy loses its armor and becomes normal enemy
            self._symbol = [['[', 'x', 'x', ']'], [' ', ']', '[', ' ']]
        if(board.numberOfEnemies <= 0):
            # All enemies dead
            return True
        return False
