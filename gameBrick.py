from gameTile import Tile


class Brick(Tile):
    def __init__(self, coordinates):
        # Initialises a brick
        # INHERITS from Tile class
        Tile.__init__(self, coordinates)
        self.isDestructible = True

    def createTile(self):
        # Representation of a brick
        tile = [['%' for x in range(4)] for y in range(2)]
        return tile
