from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Instruction:
    index: int
    value: int


@dataclass(frozen=True)
class InstructionGroup:
    mask: str
    instructions: list[Instruction]


class Part1:
    def __init__(self, ins: list[InstructionGroup]) -> None:
        self.memory = {}
        self.ins = ins

    def execute(self) -> None:
        for ig in self.ins:
            self._execute_instruction_group(ig)

    def _execute_instruction_group(self, ig: InstructionGroup) -> None:
        mask0 = int(ig.mask.replace("X", "0"), base=2)
        mask1 = int(ig.mask.replace("X", "1"), base=2)
        for ins in ig.instructions:
            masked_value = (ins.value | mask0) & mask1
            self.memory[ins.index] = masked_value

    @property
    def initialized_value(self) -> int:
        return sum(self.memory.values())


class Part2(Part1):
    def _execute_instruction_group(self, ig: InstructionGroup) -> None:
        for ins in ig.instructions:
            index_bin = format(ins.index, "036b")
            index_locs = [
                ["1"] if b == "1" else [index_bin[i]] if b == "0" else ["0", "1"]
                for i, b in enumerate(ig.mask)
            ]
            indexes = [int("".join(i), base=2) for i in product(*index_locs)]
            for index in indexes:
                self.memory[index] = ins.value


def parse_input() -> list[InstructionGroup]:
    with open("d14/input.txt", "r") as f:
        data = f.read()

    instruction_groups = []

    groups = data.split("mask")[1:]
    for group_str in groups:
        mask_str, ins_str = group_str.split("\n", maxsplit=1)
        mask = mask_str.split("=")[1].strip()

        ins: list[Instruction] = []
        for i_str in ins_str.strip().split("\n"):
            mem_index, val_str = i_str.strip().split("=")
            val = int(val_str.strip())
            index = int(mem_index.strip()[4:-1])
            ins.append(Instruction(index, val))

        instruction_groups.append(InstructionGroup(mask, ins))

    return instruction_groups


if __name__ == "__main__":
    ig = parse_input()
    part1 = Part1(ig)
    part1.execute()
    print(part1.initialized_value)

    part2 = Part2(ig)
    part2.execute()
    print(part2.initialized_value)
