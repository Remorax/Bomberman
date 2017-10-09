from gameEnemy import Enemy


class StrongEnemy(Enemy):
    def __init__(self, xinit, yinit):
        # Create a strong enemy which requires 2 explosions to be killed
        # INHERITS from Enemy class
        Enemy.__init__(self, xinit, yinit)
        self._symbol = [['|', 'x', 'x', '|'], ['|', ']', '[', '|']]
        self.descriptor = "strongEnemy"
        self.numberOfLives = 2
