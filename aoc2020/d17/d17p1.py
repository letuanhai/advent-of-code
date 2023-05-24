from typing import List, TypeVar
from copy import deepcopy


def print_dimension(d: List[List[List[bool]]]):
    for z, zi in enumerate(d):
        print(f"z = {z}")
        for row in zi:
            print("".join("#" if cell else "." for cell in row))
        print()


def count_active_neighbors2d(x: int, y: int, z: List[List[bool]]) -> int:
    count = 0
    for i in range(max(x - 1, 0), min(x + 1 + 1, len(z))):
        for j in range(max(y - 1, 0), min(y + 1 + 1, len(z[0]))):
            count += z[i][j]
    return count


T = TypeVar("T")


def expand_list(l: List[T], item: T):
    l.insert(0, deepcopy(item))
    l.append(deepcopy(item))


def grow_dimension(dimension: List[List[List[bool]]]):
    # Grow the dimension
    for zi in dimension:
        num_col = len(zi[0])
        for row in zi:
            expand_list(row, False)
        new_row = [False] * (num_col + 2)
        expand_list(zi, new_row)
    new_plane = [[False] * len(dimension[0][0]) for _ in range(len(dimension[0]))]
    expand_list(dimension, new_plane)


def execute2d(
    z: int, active_3d: List[List[List[bool]]], old_3d: List[List[List[bool]]]
):
    zi = old_3d[z]
    zim1 = old_3d[z - 1] if z > 0 else None  # z i-1
    zip1 = old_3d[z + 1] if z < len(old_3d) - 1 else None  # z i+1
    num_row = len(zi)
    num_col = len(zi[0])
    active_2d = active_3d[z]
    # Loop over rows
    for row in range(num_row):
        # Loop over cells in row
        for col in range(num_col):
            # Count active neighbors
            active_neighbors_zi = count_active_neighbors2d(row, col, zi) - int(
                zi[row][col]
            )
            active_neighbors_zim1 = (
                count_active_neighbors2d(row, col, zim1) if zim1 else 0
            )
            active_neighbors_zip1 = (
                count_active_neighbors2d(row, col, zip1) if zip1 else 0
            )
            active_neighbors = (
                active_neighbors_zi + active_neighbors_zim1 + active_neighbors_zip1
            )
            if (zi[row][col] == True) and (active_neighbors not in (2, 3)):
                active_2d[row][col] = False
            elif (zi[row][col] == False) and active_neighbors == 3:
                active_2d[row][col] = True


def execute(dimension: List[List[List[bool]]]):
    grow_dimension(dimension)

    old_dimension = deepcopy(dimension)
    # Execute cycle
    for z in range(len(dimension)):
        execute2d(z, dimension, old_dimension)


with open("d17/input.txt", "r") as f:
    data = f.readlines()

z0 = [[True if cube == "#" else False for cube in line.strip()] for line in data]

dimension = [z0]
print_dimension(dimension)


def test(z: int):
    grow_dimension(dimension)

    for i1 in range(len(dimension[0])):
        print(
            ", ".join(
                str(count_active_neighbors2d(i1, i2, dimension[z]))
                for i2 in range(len(dimension[0][0]))
            )
        )

    execute2d(z, dimension, deepcopy(dimension))


# test(0)

for _ in range(6):
    execute(dimension)

print(sum(cell for d in dimension for row in d for cell in row))
