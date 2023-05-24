with open("d13/input.txt", "r") as f:
    depart_time, bus_ids = [line.strip() for line in f.readlines()]

depart_time = int(depart_time)
bus_ids = [int(bus) for bus in bus_ids.split(",") if bus != "x"]


def earliest_bus_timestamp(bus_id: int, depart_time: int) -> int:
    return bus_id * ((depart_time // bus_id) + 1)


possible_bus_timestamp = {
    bus_id: earliest_bus_timestamp(bus_id, depart_time) for bus_id in bus_ids
}
ealiest_depart_time = min(possible_bus_timestamp.items(), key=lambda x: x[1])

print(ealiest_depart_time[0] * (ealiest_depart_time[1] - depart_time))
