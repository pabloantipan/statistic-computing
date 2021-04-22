from coordinate import Coordinate
from field import Field
from drunk import Drunk, TypicalDrunk
from bokeh.plotting import figure, show


def walking(field: Field, drunk: Drunk, steps: int):
    start = field.get_coord(drunk)
    for _ in range(steps):
        field.move_drunk(drunk)

    return start.distance(field.get_coord(drunk))


def walking_simulation(steps: int, tries_number: int, drunk_type: Drunk) -> list:
    drunk = drunk_type("David")
    origen = Coordinate(0, 0)
    distances = []

    for _ in range(tries_number):
        field = Field()
        field.add_drunken(drunk, origen)
        res_walking_simulation = walking(field, drunk, steps)
        # print(res_walking_simulation)
        distances.append(round(res_walking_simulation, 2))

    return distances


def grapher(x: list, y: list) -> None:
    graph = figure(title="drunken path", x_axis_label="steps", y_axis_label="distance")
    graph.line(x, y, legend="average distance")
    show(graph)


def main(walking_dists: list, tries_number: int, drunk_type: Drunk):
    average_distance_per_walking = []
    for steps in walking_dists:
        distances = walking_simulation(steps, tries_number, drunk_type)
        # print(distances)
        average_distance = round(sum(distances) / len(distances), 4)
        average_distance_per_walking.append(average_distance)
        max_distance = max(distances)
        min_distance = min(distances)
        print(f"{drunk_type.__name__} ramdomly walked for {steps} steps")
        print(f"Average distance = {average_distance}")
        print(f"Maxium distance = {max_distance}")
        print(f"Minimun distance = {min_distance}")

    grapher(walking_dists, average_distance_per_walking)


if __name__ == "__main__":
    walking_distance = [10, 10 ** 2, 10 ** 3, 10 ** 4]
    tries_number = 10 ** 2
    # drunk = TypicalDrunk("Paul")
    main(walking_distance, tries_number, TypicalDrunk)
