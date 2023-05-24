from dataclasses import dataclass


@dataclass
class Row:
    lower: int = 0
    upper: int = 127

    @property
    def spread(self) -> int:
        return self.upper - self.lower

    def resolve(self, seat_spec: str):
        assert seat_spec in ["F", "B"], "Invalid seat specification"
        if seat_spec == "F":
            self.upper -= self.spread // 2 + 1
        else:
            self.lower += self.spread // 2 + 1


@dataclass
class Column(Row):
    upper: int = 7

    def resolve(self, seat_spec: str):
        assert seat_spec in ["L", "R"], "Invalid seat specification"
        if seat_spec == "L":
            self.upper -= self.spread // 2 + 1
        else:
            self.lower += self.spread // 2 + 1


@dataclass
class Seat:
    row: int
    col: int

    @property
    def id(self) -> int:
        return self.row * 8 + self.col

    def __init__(self, seat_str: str) -> None:
        assert len(seat_str) == 10, "Invalid seat specification"
        row_str = seat_str[:7]
        col_str = seat_str[-3:]
        row = Row()
        col = Column()
        for c in row_str:
            row.resolve(c)
        for c in col_str:
            col.resolve(c)

        self.row = row.upper
        self.col = col.upper


def main():
    with open("d5/d5.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    all_seats = [Seat(line) for line in lines]
    all_seat_ids = [s.id for s in all_seats]
    print(max(all_seat_ids))
    print(set(range(min(all_seat_ids), max(all_seat_ids))).difference(all_seat_ids))


if __name__ == "__main__":
    main()
