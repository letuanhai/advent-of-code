from dataclasses import dataclass
from math import radians, sin, cos, atan2, sqrt


@dataclass
class Instruction:
    action: str
    value: int

    def __init__(self, instruction: str) -> None:
        self.action = instruction[0]
        self.value = int(instruction[1:])


@dataclass
class Ship:
    east: int = 0  # the ship's x axis
    north: int = 0  # the ship's y axis

    # waypoint position relative to the ship
    w_east: int = 10
    w_north: int = 1

    def move(self, ins: Instruction) -> None:
        if ins.action == "N":
            self.w_north += ins.value
        elif ins.action == "S":
            self.w_north -= ins.value
        elif ins.action == "E":
            self.w_east += ins.value
        elif ins.action == "W":
            self.w_east -= ins.value
        elif ins.action == "L":
            self._set_waypoint(ins.value)
        elif ins.action == "R":
            self._set_waypoint(-ins.value)
        elif ins.action == "F":
            self.east += self.w_east * ins.value
            self.north += self.w_north * ins.value

    def _set_waypoint(self, angle: int) -> None:
        waypoint_angle = atan2(self.w_north, self.w_east)
        waypoint_angle += radians(angle)
        l = sqrt(self.w_east**2 + self.w_north**2)
        self.w_east = round(l * cos(waypoint_angle))
        self.w_north = round(l * sin(waypoint_angle))

    @property
    def distance(self) -> int:
        return abs(self.east) + abs(self.north)


def main():
    with open("./d12/input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    instructions = [Instruction(line) for line in data]
    ship = Ship()
    for ins in instructions:
        ship.move(ins)
    print(ship.distance)


if __name__ == "__main__":
    main()
