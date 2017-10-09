from gameEnemy import Enemy


class FastEnemy(Enemy):
    def __init__(self, xinit, yinit):
        # Create an enemy, which moves twice as fast as normal enemies
        # INHERITS from Enemy class
        Enemy.__init__(self, xinit, yinit)
        self._symbol = [['[', '>', '>', ']'], [' ', '/', '/', ' ']]
        self.descriptor = "fastEnemy"
        self.numberOfLives = 1
