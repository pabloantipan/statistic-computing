class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x:{self.x}, y:{self.y})"

    def move(self, dx: float, dy: float) -> any:
        """
        :args:
            dx: delta x displacement
            dy: delta y displacement
        :raises:
            none, for now
        :returns:
            Coordinate instante wih new position
        """
        return Coordinate(self.x + dx, self.y + dy)

    def distance(self, r: "Coordinate") -> float:
        dx = self.x - r.x
        dy = self.y - r.y

        result = (dx ** 2 + dy ** 2) ** 0.5
        # print("dist", result)
        return result
