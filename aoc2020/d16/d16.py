import itertools
from dataclasses import dataclass
import functools
import math


@dataclass(frozen=True)
class RuleGroup:
    lower: int
    upper: int

    def is_valid(self, num: int) -> bool:
        return num in range(self.lower, self.upper + 1)


@dataclass(frozen=True)
class RulePosition:
    rule_groups: list[RuleGroup]

    def is_valid(self, num: int) -> bool:
        return any(rg.is_valid(num) for rg in self.rule_groups)


def find_invalid_values(
    ticket_rules: list[RulePosition], ticket: list[int]
) -> list[int]:
    invalid_nums = []
    for num in ticket:
        if not any(pos.is_valid(num) for pos in ticket_rules):
            invalid_nums.append(num)
    return invalid_nums


def is_valid_ticket(ticket_rules: list[RulePosition], ticket: list[int]) -> bool:
    if find_invalid_values(ticket_rules, ticket):
        return False
    return True


with open("d16/input.txt", "r") as f:
    data = f.read()
rule_str, my_ticket_str, nearby_tickets_data = data.split("\n\n")
field_names = []
rules: list[RulePosition] = []
for r in rule_str.strip().split("\n"):
    name, rule_pos = r.strip().split(": ")
    field_names.append(name.strip())
    rule_groups: list[RuleGroup] = []
    for group_str in rule_pos.strip().split(" or "):
        lower, upper = group_str.strip().split("-")
        rule_groups.append(RuleGroup(int(lower.strip()), int(upper.strip())))
    rules.append(RulePosition(rule_groups))

nearby_tickets: list[list[int]] = [
    [int(num.strip()) for num in ticket.strip().split(",")]
    for ticket in nearby_tickets_data.strip().split("\n")[1:]
]
my_tickets: list[list[int]] = [
    [int(num.strip()) for num in ticket.strip().split(",")]
    for ticket in my_ticket_str.strip().split("\n")[1:]
]


def part_1():
    print(
        sum(
            itertools.chain(
                *[find_invalid_values(rules, ticket) for ticket in nearby_tickets]
            )
        )
    )


def part_2():
    valid_tickets = [
        ticket for ticket in nearby_tickets if is_valid_ticket(rules, ticket)
    ] + my_tickets
    possible_pos = []
    for rp in rules:
        valid_pos = set(
            [
                i
                for i in range(len(rules))
                if all(rp.is_valid(ticket[i]) for ticket in valid_tickets)
            ]
        )
        possible_pos.append(valid_pos)

    while any(len(pos) != 1 for pos in possible_pos):
        for i, pos in enumerate(possible_pos):
            if len(pos) == 1:
                continue
            possible_pos[i] = functools.reduce(
                lambda pos, other_pos: pos.difference(other_pos)
                if pos.difference(other_pos)
                else pos,
                possible_pos,
                pos,
            )
    field_position = list(itertools.chain(*possible_pos))
    my_ticket = my_tickets[0]
    my_ticket_value = {
        name: my_ticket[field_position[i]] for i, name in enumerate(field_names)
    }
    print(
        math.prod([v for k, v in my_ticket_value.items() if k.startswith("departure")])
    )


if __name__ == "__main__":
    part_1()
    part_2()
