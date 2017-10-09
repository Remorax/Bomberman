class Tile():
    def __init__(self, coordinates):
        self._coordinates = coordinates
        ''' The coordinates are ENCAPSULATED so it can't be directly accessed
        as an attribute of the instance'''
        self._xcoord = coordinates[0]
        self._ycoord = coordinates[1]
        self.isDestructible = False
        self.tileRepresentation = self.createTile()

    def __repr__(self):
        tile = self.createTile()
        return str(tile)

    def getXCoordinate(self):
        return self._xcoord

    def getYCoordinate(self):
        return self._ycoord

    def createTile(self):
        tile = [[' ' for x in range(4)] for y in range(2)]
        return tile
