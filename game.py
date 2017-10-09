# import external modules

import os
import random
import getch
import types

from random import randint
from lazyme.string import color_print
from operator import itemgetter
from imp import reload

from gameBomb import Bomb
from gameSpeedPowerup import speedPowerup
from gameWallpassPowerup import wallpassPowerup
from gameExplosionPowerup import explosionPowerup
from gameImmortalityPowerup import immortalityPowerup

from gameBoard import board, boardRows, boardCols

from gameEnemy import Enemy
from gameFastEnemy import FastEnemy
from gameStrongEnemy import StrongEnemy
from gameBomberman import bomberman

import gameBomberman
import gameEnemy
import gameBomb
import gameBoard
import gameExplosionPowerup
import gameImmortalityPowerup
import gameSpeedPowerup
import gameWallpassPowerup


# Starts the game
def start():
    bomberman.checkForDeath = types.MethodType(checkForDeath, bomberman)
    bomberman.handleBombermanMovement =\
        types.MethodType(handleBombermanMovement, bomberman)
    bomberman.generatePowerupPosition =\
        types.MethodType(generatePowerupPosition, bomberman)
    bomberman.generatePowerup =\
        types.MethodType(generatePowerup, bomberman)
    board.handleWallpassPowerup =\
        types.MethodType(handleWallpassPowerup, board)
    board.createBoard()  # creates and prints the board
    # create different types of enemies based on the initial coordinates
    board.enemiesArray = [Enemy(x[0], x[1]) if((x[0] + x[1]) % 3 == 1)
                          else StrongEnemy(x[0], x[1])
                          if((x[0] + x[1]) % 3 == 2)
                          else FastEnemy(x[0], x[1]) for x in board.enemies]

    startGame()


def startGame():
    # The main loop where each iteration is a frame of the game
    while (True):
        # function call to bomberman's movement
        op = bomberman.handleBombermanMovement()
        if(op == 'Quit'):
            # On pressing 'Esc'
            os.system('tput reset')
            color_print("Game ended by user!", color='red', bold=True)
            break
        if(bomberman.activeBomb is True):
            bomberman.activeBomb = False
        resultList = []
        resultList2 = []
        for enemy in board.enemiesArray:
            # check for death of enemy/bomberman after bomberman's movement
            result = bomberman.checkForDeath(enemy)
            resultList.append(result)
            if(not result[0]):
                # Game is not over, so allow enemy to move

                # call function for random movement of enemy
                (deltax, deltay) = enemy.getPseudoRandomInteger()
                if(enemy.descriptor == 'fastEnemy'):
                    # If the enemy is a 'FastEnemy', he moves twice as fast
                    if(abs(deltax) > 0):
                        deltax *= 2
                    else:
                        deltay *= 2
                    validInput = False
                    while (not validInput):
                        validInput = enemy.move(deltax, deltay)
                else:
                    # moves the enemy given deltax and deltay
                    enemy.move(deltax, deltay)
                # check for death of enemy/bomberman after enemy's movement
                result2 = bomberman.checkForDeath(enemy)
                resultList2.append(result2)
        try:
            result = max(resultList, key=itemgetter(1))
        except:
            pass
        try:
            result2 = max(resultList2, key=itemgetter(1))
        except:
            pass
        for x in list(resultList + resultList2):
            if(x[2]):
                for powerup in self.activePowerups:
                    if(powerup.descriptor == 'immortality'):
                        ''' Decrement moves left if player has immortality
                        powerup '''
                        powerup.movesLeft = str(int(powerup.movesLeft) - 1)
                        break
        ''' Update livesLeft according to the results obtained from the
            checkForDeath function'''
        for (i, x) in enumerate(resultList):
            if(x[3]):
                board.livesLeft = (int(board.livesLeft) - 1)\
                    if(int(board.livesLeft) > 0) else 0
                board.livesLeft = "0" + str(board.livesLeft)
                break
        for (i, x) in enumerate(resultList2):
            if(not resultList[i][3] and x[3]):
                board.livesLeft = int(board.livesLeft) - 1\
                    if(int(board.livesLeft) > 0) else 0
                board.livesLeft = "0" + str(board.livesLeft)
                break
        boardArray = board.getBoardArray()
        os.system('tput reset')
        color_print("SCORE: " + board.score, color='yellow',  end='',
                    bold=True)
        color_print("\t\t\t\t\t   LIVES: " + board.livesLeft,
                    color='yellow', bold=True)
        # Prints the board
        for row in boardArray:
            for tile in row:
                string = ''.join(tile[0])
                if(string == '####'):
                    color_print('    ', color='gray', highlight='gray',
                                end='', bold=True)
                elif(string == "%%%%"):
                    color_print('~~~~', color='red', highlight='yellow',
                                end='', bold=True)
                elif(string == '[^^]'):
                    color_print(string, color='blue', highlight='cyan',
                                end='', bold=True)
                elif(string == '[xx]' or string == '[>>]' or string == '|xx|'):
                    color_print(string, color='red', highlight='green',
                                end='', bold=True)
                elif(string == '    '):
                    color_print(string, color='black', highlight='black',
                                end='', bold=True)
                else:
                    color_print(string, color='red', end='', bold=True)
            print("\n", end='')
            for tile in row:
                string = ''.join(tile[1])
                if(string == '####'):
                    color_print('    ', color='gray', highlight='gray', end='',
                                bold=True, underline=True)
                elif(string == "%%%%"):
                    color_print('~~~~', color='red', highlight='yellow',
                                end='', bold=True, underline=True)
                elif(string == ' ][ ' or string == '|][|' or string == ' // '):
                    if(''.join(tile[0]) == '[^^]'):
                        color_print(string, color='blue', highlight='cyan',
                                    end='', bold=True)
                    else:
                        color_print(string, color='red', highlight='green',
                                    end='', bold=True)
                elif(string == '    '):
                    color_print(string, color='black', highlight='black',
                                end='', bold=True, underline=True)
                else:
                    color_print(string, color='red', end='', bold=True)
            print("\n", end='')
        # If game is over, print the final outcome
        try:
            if(result[0]):
                color_print(result[0], color='red', bold=True)
                break
        except:
            pass
        try:
            if(result2[0]):
                color_print(result2[0], color='red', bold=True)
                break
        except:
            pass
        if(bomberman.detonatedBomb):
            # If bomb has been detonated, clear it after showing explosion
            for (x, y) in board.blastRadius:
                boardArray = board.getBoardArray()
                boardArray[y][x] = [[' ' for i in range(4)] for j in range(2)]
                board.setBoardArray(boardArray)
            board.blastRadius = []
            bomberman.detonatedBomb = False
    return


def checkForDeath(self, enemy):
    ''' Uses POLYMORPHISM to get the x and y coordinates as both
    bomberman and enemy have these methods'''

    xcoord = self.getXCoordinate()
    ycoord = self.getYCoordinate()
    xenemy = enemy.getXCoordinate()
    yenemy = enemy.getYCoordinate()
    powerupApplied = False
    for powerup in self.activePowerups:
        if(powerup.descriptor == "immortality"):
            if(int(powerup.movesLeft) > 0):
                board.livesLeft = "INF"
                powerupApplied = True
            else:
                board.livesLeft = "01"
                self.activePowerups.remove(powerup)
    if((xcoord, ycoord) in board.blastRadius):
        if((xenemy, yenemy) in board.blastRadius):
            # Enemy as well as bomberman in bomb's blast radius

            # Update score
            board.score = str(int(board.score) + 50)
            # Kill enemy
            gameOver = enemy.destroyEnemy()
            if(not powerupApplied):
                if(gameOver):
                    return ("You killed all the enemies, but you\
                            killed yourself as well.\
                            The game is a tie :P", 3, powerupApplied, True)
                else:
                    return ("You killed one or more enemies, but you martyred\
                            yourself in the process. You lose :(", 2,
                            powerupApplied, True)
            else:
                # Player has immortality powerup, so only enemies die
                if(gameOver):
                    return ("You killed all the enemies. Congrats, you win!!\
                            :D", 3, powerupApplied, False)
                else:
                    return(True, -1, powerupApplied, False)
        else:
            if (not powerupApplied):
                # Player killed due to explosion from bomb
                return ("You killed yourself *facepalm*. You lose the game :(",
                        1, powerupApplied, True)
    elif((xenemy, yenemy) in board.blastRadius):
        # Enemy in bomb's blast radius

        # Update score
        board.score = str(int(board.score) + 50)
        # Kill enemy
        gameOver = enemy.destroyEnemy()
        if(gameOver):
            # All enemies dead
            return ("You killed all the enemies. Congrats, you win!! :D",
                    3, powerupApplied, False)
        else:
            # Some enemies dead
            return(True, -1, powerupApplied, False)
    elif((xcoord, ycoord) == (xenemy, yenemy)):
        # Enemy collides with bomberman, so bomberman dies
        if(not powerupApplied):
            return ("The enemy killed you. You lose! :(", 1,
                    powerupApplied, True)
    return (False, 0, powerupApplied, False)


def generatePowerupPosition(self):
    # A function to randomly generate Powerup Position
    ''' Uses POLYMORPHISM to get the x and y coordinates as both
    bomberman and enemy have these methods'''
    xcurrent = self.getXCoordinate()
    ycurrent = self.getYCoordinate()
    excludedList = []
    excludedList.append((xcurrent, ycurrent))
    for enemy in board.enemiesArray:
        xenemy = enemy.getXCoordinate()
        yenemy = enemy.getYCoordinate()
        excludedList.append((xenemy, yenemy))
    excludedList.extend([(a[0].getXCoordinate(), a[0].getYCoordinate())
                         for a in self.activeBombs])
    # Exclude positions of bomberman, enemies and active bombs
    possiblePowerupPositionList = list(set(board.unoccupiedPositions) -
                                       set(excludedList))
    possiblePowerupPositionList = [possiblePowerupPosition for
                                   possiblePowerupPosition in
                                   possiblePowerupPositionList if
                                   abs(possiblePowerupPosition[0] - xcurrent) <
                                   5 and abs(possiblePowerupPosition[1] -
                                             ycurrent) < 5]

    randomPosition = random.randint(0, len(possiblePowerupPositionList) - 1)
    return possiblePowerupPositionList[randomPosition]


def handleWallpassPowerup(self):
    # A utility function called to handle wallpass powerup
    for powerup in bomberman.activePowerups:
        if(powerup.descriptor == "wallpass"):
            if(int(powerup.movesLeft) > 0):
                powerup.movesLeft = str(int(powerup.movesLeft) - 1)
                return True
            else:
                bomberman.activePowerups.remove(powerup)
                self.wallpass = False
                self.isTemporaryWall = False
                self.temporaryWall = ('', '')
    return False


def generatePowerup(self):
    # Generate a pseudo Random Powerup based on score
    if(int(board.score) < 20):
        return False
    if(int(board.score) >= 20 and int(board.score) < 30):
        powerupNumber = 0
        pointsNeeded = 20
    elif(int(board.score) >= 30 and int(board.score) < 40):
        powerupNumber = randint(0, 1)
        pointsNeeded = 30 if powerupNumber == 1 else 20
    elif(int(board.score) >= 40 and int(board.score) < 60):
        powerupNumber = randint(0, 2)
        pointsDict = {2: 40, 1: 30, 0: 20}
        pointsNeeded = pointsDict[powerupNumber]
    else:
        powerupNumber = randint(0, 3)
        pointsDict = {3: 60, 2: 40, 1: 30, 0: 20}
        pointsNeeded = pointsDict[powerupNumber]

    temp = board.score
    board.score = str(int(board.score) - pointsNeeded)
    if(int(board.score) < 0):
        board.score = temp
        return False
    if(int(board.score) < 10):
        board.score = "0" + board.score
    (randomx, randomy) = self.generatePowerupPosition()
    # Instantiate powerup accordingly
    if(powerupNumber == 0):
        self.powerup = speedPowerup((randomx, randomy))
    elif(powerupNumber == 1):
        self.powerup = wallpassPowerup((randomx, randomy))
    elif(powerupNumber == 2):
        self.powerup = explosionPowerup((randomx, randomy))
    elif(powerupNumber == 3):
        self.powerup = immortalityPowerup((randomx, randomy))
    self.createdPowerups.append(self.powerup)
    return True


def handleBombermanMovement(self):
    while (1):
        validInput = False
        ''' Uses POLYMORPHISM to get the x and y coordinates as both
        bomberman and enemy have these methods'''
        xold = self.getXCoordinate()
        yold = self.getYCoordinate()
        color_print("Your move:\n(Controls: W(up) A(left) S(right) D(down)" +
                    "B(drop bomb) P(get a powerup) Q(stay there) Esc(to quit)",
                    end='\n', color='red', bold=True)
        while (not validInput):
            key = getch.getch()  # Get input from user
            powerupApplied = False
            if(key == 'w' or key == 'W'):
                for powerup in self.activePowerups:
                    if(powerup.descriptor == "speed"):
                        # If player has speed powerup, move twice as fast
                        if(int(powerup.movesLeft) > 0):
                            ''' Uses POLYMORPHISM as the move method is used
                             for both enemy and bomberman'''
                            validInput = self.move(0, -2)
                            powerup.movesLeft = str(int(powerup.movesLeft) - 1)
                            powerupApplied = True
                        else:
                            self.activePowerups.remove(powerup)
                if(not powerupApplied):
                    ''' Uses POLYMORPHISM as the move method is used
                        for both enemy and bomberman'''
                    validInput = self.move(0, -1)
            elif(key == 's' or key == 'S'):
                for powerup in self.activePowerups:
                    if(powerup.descriptor == "speed"):
                        # If player has speed powerup, move twice as fast
                        if(int(powerup.movesLeft) > 0):
                            ''' Uses POLYMORPHISM as the move method is used
                             for both enemy and bomberman'''
                            validInput = self.move(0, 2)
                            powerup.movesLeft = str(int(powerup.movesLeft) - 1)
                            powerupApplied = True
                        else:
                            self.activePowerups.remove(powerup)
                if(not powerupApplied):
                    ''' Uses POLYMORPHISM as the move method is used
                        for both enemy and bomberman'''
                    validInput = self.move(0, 1)
            elif(key == 'a' or key == 'A'):
                for powerup in self.activePowerups:
                    if(powerup.descriptor == "speed"):
                        # If player has speed powerup, move twice as fast
                        if(int(powerup.movesLeft) > 0):
                            ''' Uses POLYMORPHISM as the move method is used
                             for both enemy and bomberman'''
                            validInput = self.move(-2, 0)
                            powerup.movesLeft = str(int(powerup.movesLeft) - 1)
                            powerupApplied = True
                        else:
                            self.activePowerups.remove(powerup)
                if(not powerupApplied):
                    ''' Uses POLYMORPHISM as the move method is used
                        for both enemy and bomberman'''
                    validInput = self.move(-1, 0)
            elif(key == 'd' or key == 'D'):
                for powerup in self.activePowerups:
                    if(powerup.descriptor == "speed"):
                        # If player has speed powerup, move twice as fast
                        if(int(powerup.movesLeft) > 0):
                            validInput = self.move(2, 0)
                            powerup.movesLeft = str(int(powerup.movesLeft) - 1)
                            powerupApplied = True
                        else:
                            self.activePowerups.remove(powerup)
                if(not powerupApplied):
                    ''' Uses POLYMORPHISM as the move method is used
                        for both enemy and bomberman'''
                    validInput = self.move(1, 0)
            elif(key == 'b' or key == 'B'):
                for powerup in self.activePowerups:
                    if(powerup.descriptor == "explosion"):
                        ''' If player has explosion powerup, create a bomb which
                            is twice as powerful '''
                        if(int(powerup.movesLeft) > 0):
                            bomb = Bomb((xold, yold), True)
                            powerup.movesLeft = str(int(powerup.movesLeft) - 1)
                            powerupApplied = True
                        else:
                            self.activePowerups.remove(powerup)
                if(not powerupApplied):
                    # Create a normal bomb in the absence of explosion powerup
                    bomb = Bomb((xold, yold), False)
                bomberman.activeBomb = True
                self.activeBombs.append((bomb, 3))
                validInput = True
            elif(key == 'q' or key == 'Q'):
                validInput = True
                # Bomberman stays at the same position
            elif(key == 'p' or key == 'P'):
                # Generate a powerup
                validInput = self.generatePowerup()
            elif(key == '\x1b'):
                # Quit the game if 'Esc' is pressed
                return "Quit"

        for powerup in self.createdPowerups:
            if(powerup.powerupCreated):
                powerup.powerupCreated = False
            else:
                ''' Uses POLYMORPHISM to get the x and y coordinates as both
                    powerup, wall and brick all have these methods from Tile
                    class'''
                if((powerup.getXCoordinate(), powerup.getYCoordinate()) ==
                   (self.getXCoordinate(),  self.getYCoordinate())):
                    # If player collects the powerup
                    powerupDict = {'speed': '8', 'explosion': '2',
                                   'immortality': '3', 'wallpass': '10'}
                    powerup.movesLeft = powerupDict[powerup.descriptor]
                    ''' If there is already an active powerup of the same type,
                     replace it with the new one '''
                    for activePowerup in self.activePowerups:
                        if(activePowerup.descriptor == powerup.descriptor):
                            self.activePowerups.remove(activePowerup)
                    # Powerup is active!
                    self.activePowerups.append(powerup)
                    self.createdPowerups.remove(powerup)
                    if(powerup.descriptor == 'wallpass'):
                        board.wallpass = True
                else:
                    enemyOnPowerup = False
                    for enemy in board.enemiesArray:
                        ''' Uses POLYMORPHISM to get the x and y coordinates as both
                        bomberman and enemy have these methods'''
                        if((enemy.getXCoordinate(), enemy.getYCoordinate()) ==
                            (powerup.getXCoordinate(),
                             powerup.getYCoordinate())):
                            ''' If enemy reaches the uncollected powerup,
                             it should be destroyed '''
                            enemyOnPowerup = True
                            self.createdPowerups.remove(powerup)
                            powerup.destroyPowerup()
                            break
                    if(not enemyOnPowerup):
                        if(int(powerup.counter) > 0):
                            powerup.counter = str(int(powerup.counter) - 1)
                            powerup.showPowerup()
                        else:
                            ''' Bomberman did not collect powerup in time,
                             so destroy it '''
                            powerup.destroyPowerup()
                            self.createdPowerups.remove(powerup)

        for (index, bombs) in enumerate(self.activeBombs):
            currentCounter = bombs[1]
            if(currentCounter == 0):
                # If bomb timer reaches 0, detonate bomb.
                bombs[0].detonate()
                self.activeBombs.remove(bombs)
                bombs[0].detonated = True
                self.detonatedBomb = bombs[0]
            else:
                # Else update the counter
                self.activeBombs[index] = (bombs[0], bombs[1] - 1)
                bombs[0].startBombTimer(str(bombs[1] - 1))
        if(validInput):
            break
    return


start()
