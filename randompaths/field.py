from drunk import Drunk, TypicalDrunk
from coordinate import Coordinate


class Field:
    def __init__(self):
        self.coordinates = {}

    def add_drunken(self, drunk: Drunk, coord: Coordinate) -> bool:
        """
        :args:
            drunk, Drunk instance to add
            coord, Coordinate of drunk
        :raises:
            none
        :returns:
            bool, True for testing purpose
        """
        self.coordinates[drunk] = coord
        return True

    def move_drunk(self, drunk: Drunk) -> Coordinate:
        """It moves a certain drunk along the field
        :args:
            drunk, instance of Drunk to move
        :raises:
            none
        :returns:
            instance of Coordinate with new coordinates
            after movement
        """
        dx, dy = drunk.walk()
        actual_coord = self.coordinates[drunk]
        new_coord = actual_coord.move(dx, dy)
        # print(new_coord)
        self.coordinates[drunk] = new_coord

        return new_coord

    def get_coord(self, drunk: Drunk) -> Drunk:
        """
        :args:
            drunk, instance of Drunk
        :raises:
            none
        :returns:
            instance of Coordinate with coordinate of drunk
        """
        return self.coordinates[drunk]
