from dataclasses import dataclass
from typing import List, Union


@dataclass
class Seat:
    is_occupied: bool = False
    visible_occupied_seats: int = 0


@dataclass(frozen=True)
class Floor:
    is_occupied = False


class Layout:
    def __init__(self, layout_lines: List[str]) -> None:
        self.grid: List[List[Union[Seat, Floor]]] = [
            [self._parse_spot(s) for s in line] for line in layout_lines
        ]

        self._row_nums = len(self.grid)
        self._col_nums = len(self.grid[0])
        self._update_seat_status()

    def _update_seat_status(self) -> None:
        for r in range(self._row_nums):
            for c in range(self._col_nums):
                spot = self.grid[r][c]
                if isinstance(spot, Floor):
                    continue
                adjacent_seats = [
                    self._first_visible_seat_occupied(r, c, i, j)
                    for i in range(-1, 2)
                    for j in range(-1, 2)
                    if i != 0 or j != 0
                ]
                spot.visible_occupied_seats = sum(adjacent_seats)

    def _first_visible_seat_occupied(
        self, r: int, c: int, r_offset: int, c_offset: int
    ) -> bool:
        row, col = r + r_offset, c + c_offset
        while (0 <= row < self._row_nums) and (0 <= col < self._col_nums):
            if isinstance(self.grid[row][col], Seat):
                return self.grid[row][col].is_occupied
            row += r_offset
            col += c_offset
        return False

    @staticmethod
    def _parse_spot(spot: str) -> Union[Seat, Floor]:
        if spot == ".":
            return Floor()
        elif spot == "L":
            return Seat()
        elif spot == "#":
            return Seat(is_occupied=True)
        else:
            raise Exception("Invalid position marker!!")

    def update_layout(self) -> int:
        """Update the seat layout and return number changed seat"""
        changed_seat = 0
        for r in range(self._row_nums):
            for c in range(self._col_nums):
                spot = self.grid[r][c]
                if isinstance(spot, Floor):
                    continue
                elif spot.is_occupied and spot.visible_occupied_seats >= 5:
                    spot.is_occupied = False
                    changed_seat += 1
                elif not spot.is_occupied and spot.visible_occupied_seats == 0:
                    spot.is_occupied = True
                    changed_seat += 1
        self._update_seat_status()
        return changed_seat

    @property
    def occupied_seats(self) -> int:
        return sum(s.is_occupied for r in self.grid for s in r)

    def __repr__(self) -> str:
        layout = ""
        for r in self.grid:
            row = ""
            for spot in r:
                if isinstance(spot, Floor):
                    row += "."
                elif spot.is_occupied:
                    row += "#"
                else:
                    row += "L"
            layout += row + "\n"
        return layout


def main():
    with open("d11/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    l = Layout(lines)
    while l.update_layout() > 0:
        continue
    print(l.occupied_seats)


if __name__ == "__main__":
    main()
