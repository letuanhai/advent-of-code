from dataclasses import dataclass
from typing import List
from functools import reduce


@dataclass
class Point:
    is_tree: bool


@dataclass
class Slope:
    x_slope: int
    y_slope: int


class Map:
    def __init__(self, map_lines: List[str]) -> None:
        # each line in map: ...#...#....#....##...###....#.
        self.map_points: List[List[Point]] = []
        self.max_x = len(map_lines[0])
        self.max_y = len(map_lines)
        for line in map_lines:
            map_line: List[Point] = []
            for square in line:
                is_tree = square == "#"
                map_line.append(Point(is_tree))
            self.map_points.append(map_line)

    def count_trees(self, slope: Slope) -> int:
        count = 0
        x = slope.x_slope
        y = slope.y_slope
        while y < self.max_y:
            x_coord = x % self.max_x if x >= self.max_x else x
            count += self.map_points[y][x_coord].is_tree
            x += slope.x_slope
            y += slope.y_slope
        return count


def main():

    with open("d3.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    map = Map(lines)
    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
    print(reduce(lambda x, y: x * y, [map.count_trees(slope) for slope in slopes], 1))


if __name__ == "__main__":
    main()
