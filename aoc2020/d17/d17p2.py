from typing import Set, NamedTuple
import itertools


class Point(NamedTuple):
    x: int
    y: int
    z: int
    w: int


class Boundary(NamedTuple):
    lower: int
    upper: int


class DimensionBoundary(NamedTuple):
    x: Boundary
    y: Boundary
    z: Boundary
    w: Boundary


class Dimension:
    def __init__(self) -> None:
        with open("d17/input.txt", "r") as f:
            data = f.readlines()

        self._active_points: Set[Point] = {
            Point(x, y, 0, 0)
            for y, line in enumerate(data)
            for x, cell in enumerate(line)
            if cell == "#"
        }

    @property
    def _boundary(self) -> DimensionBoundary:
        return DimensionBoundary(
            *[
                Boundary(min(dimension), max(dimension))
                for dimension in zip(*self._active_points)
            ]
        )

    def __repr__(self) -> str:
        s = ""
        for z in range(self._boundary.z.lower, self._boundary.z.upper + 1):
            s += f"z = {z}\n"
            for y in range(self._boundary.y.lower, self._boundary.y.upper + 1):
                s += (
                    "".join(
                        "#" if (x, y, z) in self._active_points else "."
                        for x in range(
                            self._boundary.x.lower, self._boundary.x.upper + 1
                        )
                    )
                    + "\n"
                )
            s += "\n"
        return s

    @property
    def active_points_num(self) -> int:
        return len(self._active_points)

    def _count_active_neighbors(self, p: Point) -> int:
        all_neighbors = [
            Point(*c)
            for c in itertools.product(*[[d + i for i in range(-1, 2)] for d in p])
        ]  # including itself
        return sum(
            1 if c in self._active_points and c != p else 0 for c in all_neighbors
        )

    def _expand_boundary(self) -> DimensionBoundary:
        return DimensionBoundary(
            *[Boundary(lower=c.lower - 1, upper=c.upper + 1) for c in self._boundary]
        )

    def execute_cycle(self) -> None:
        expanded_points = [
            Point(*c)
            for c in itertools.product(
                *[list(range(c.lower, c.upper + 1)) for c in self._expand_boundary()]
            )
        ]
        next_cycle_active_points = set()
        for p in expanded_points:
            active_neighbors = self._count_active_neighbors(p)
            if p in self._active_points and active_neighbors in (2, 3):
                next_cycle_active_points.add(p)
            elif p not in self._active_points and active_neighbors == 3:
                next_cycle_active_points.add(p)
        self._active_points = next_cycle_active_points


d = Dimension()
for _ in range(6):
    d.execute_cycle()
print(d.active_points_num)
