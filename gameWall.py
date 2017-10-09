from gameTile import Tile


class Wall(Tile):
    def __init__(self, coordinates):
        # Initialises a wall
        # INHERITS from Tile class
        Tile.__init__(self, coordinates)

    def createTile(self):
        # Representation of a wall
        tile = [['#' for x in range(4)] for y in range(2)]
        return tile
