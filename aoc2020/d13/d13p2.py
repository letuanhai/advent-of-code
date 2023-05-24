from typing import NamedTuple
import math


class Bus(NamedTuple):
    id: int
    offset: int


with open("d13/input.txt", "r") as f:
    depart_time, bus_ids = [line.strip() for line in f.readlines()]

# bus_ids = "17,x,13,19"

bus_ids = [Bus(int(v), i) for i, v in enumerate(bus_ids.split(",")) if v != "x"]

bus_ids.sort(reverse=True)

import pdb

pdb.set_trace()

timestamp = bus_ids[0].id
step = bus_ids[0].id
satisfied_bus_ids = [bus_ids[0]]
for bus_id in bus_ids[1:]:
    satisfied_bus_ids.append(bus_id)
    while True:
        if all(
            (timestamp - bus_ids[0].offset + bus_id.offset) % bus_id.id == 0
            for bus_id in satisfied_bus_ids
        ):
            break
        timestamp += step
    step = math.lcm(*[b.id for b in satisfied_bus_ids])

print(timestamp - bus_ids[0].offset)
