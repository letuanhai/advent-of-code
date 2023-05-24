from dataclasses import dataclass
from typing import List, Union


@dataclass
class Seat:
    is_occupied: bool = False
    occupied_adjacent_seats: int = 0


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
                else:
                    adjacent_seats = [
                        self.grid[i][j].is_occupied
                        for i in range(max(0, r - 1), min(r + 1 + 1, self._row_nums))
                        for j in range(max(0, c - 1), min(c + 1 + 1, self._col_nums))
                        if i != r or j != c
                    ]
                    spot.occupied_adjacent_seats = sum(adjacent_seats)

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
                elif spot.is_occupied and spot.occupied_adjacent_seats >= 4:
                    spot.is_occupied = False
                    changed_seat += 1
                elif not spot.is_occupied and spot.occupied_adjacent_seats == 0:
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
