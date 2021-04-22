from random import choice


class Drunk:
    def __init__(self, name):
        self.name = name


class TypicalDrunk(Drunk):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        result = choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        # print(result)
        return result
