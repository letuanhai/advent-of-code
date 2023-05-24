from __future__ import annotations
from typing import Optional, List, Dict, ClassVar
from dataclasses import dataclass


@dataclass
class Bag:
    all_bags: ClassVar[Dict[str, Bag]] = {}
    name: str
    child_bags: Dict[str, int]

    def __init__(self, bag_rule: str) -> None:
        """bag_rule example: dark orange bags contain 3 bright white bags, 4 muted yellow bags."""
        bag_name_str, child_bags_str = bag_rule.split(" contain ")
        bag_name, _ = bag_name_str.rsplit(" ", maxsplit=1)
        self.name = bag_name
        child_bags = {}
        if not child_bags_str.startswith("no"):
            for bag_str in child_bags_str.split(", "):
                bag_name_str, _ = bag_str.rsplit(" ", maxsplit=1)
                num, name = bag_name_str.split(" ", maxsplit=1)
                child_bags[name] = int(num)

        self.child_bags = child_bags
        type(self).all_bags[bag_name] = self

    def contain_bag(self, child_name: str) -> bool:
        if child_name in self.child_bags:
            return True
        return any(
            Bag.all_bags[child].contain_bag(child_name)
            for child in self.child_bags
            if child in Bag.all_bags
        )

    @property
    def num_nested_bags(self) -> int:
        num_bags = sum(self.child_bags.values())
        num_bags += sum(
            type(self).all_bags[child].num_nested_bags * self.child_bags[child]
            for child in self.child_bags
            if child in type(self).all_bags
        )
        return num_bags


def main():
    with open("d7/d7.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    [Bag(line) for line in lines]
    print(sum(bag.contain_bag("shiny gold") for bag in Bag.all_bags.values()))
    print(Bag.all_bags["shiny gold"].num_nested_bags)


if __name__ == "__main__":
    main()
