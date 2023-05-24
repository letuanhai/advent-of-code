from dataclasses import dataclass
from math import radians, sin, cos


@dataclass
class Instruction:
    action: str
    value: int

    def __init__(self, instruction: str) -> None:
        self.action = instruction[0]
        self.value = int(instruction[1:])


@dataclass
class Ship:
    east: int = 0  # x axis
    north: int = 0  # y axis
    # the ship starts by facing east
    angle = 0
    east_offset: int = 1
    north_offset: int = 0

    def move(self, ins: Instruction) -> None:
        if ins.action == "N":
            self.north += ins.value
        elif ins.action == "S":
            self.north -= ins.value
        elif ins.action == "E":
            self.east += ins.value
        elif ins.action == "W":
            self.east -= ins.value
        elif ins.action == "L":
            self.angle += ins.value
            self.east_offset = int(cos(radians(self.angle)))
            self.north_offset = int(sin(radians(self.angle)))
        elif ins.action == "R":
            self.angle -= ins.value
            self.east_offset = int(cos(radians(self.angle)))
            self.north_offset = int(sin(radians(self.angle)))
        elif ins.action == "F":
            self.east += ins.value * self.east_offset
            self.north += ins.value * self.north_offset


def main():
    with open("./d12/input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
    instructions = [Instruction(line) for line in data]
    ship = Ship()
    for ins in instructions:
        ship.move(ins)
    print(abs(ship.east) + abs(ship.north))


if __name__ == "__main__":
    main()
