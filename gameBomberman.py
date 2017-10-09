from gamePerson import Person


class Bomberman(Person):
    def __init__(self, xinit, yinit):
        # INHERITS from Person class
        Person.__init__(self, xinit, yinit)
        self.activeBomb = False
        self.detonatedBomb = False
        ''' The symbol is ENCAPSULATED so it can't be directly accessed
        as an attribute of the instance'''
        self._symbol = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]
        self.activeBombs = []
        self.activePowerups = []
        self.createdPowerups = []


bomberman = Bomberman(1, 1)
