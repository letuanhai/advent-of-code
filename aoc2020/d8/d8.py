from dataclasses import dataclass, field
from typing import Dict, Callable, List


@dataclass
class Instruction:
    operation: str
    arg: int

    def __init__(self, ins_line: str) -> None:
        operation, arg = ins_line.split(" ")
        self.operation = operation
        self.arg = int(arg)

    def flip_nop_jmp(self) -> None:
        if self.operation == "nop":
            self.operation = "jmp"
        elif self.operation == "jmp":
            self.operation = "nop"


@dataclass
class Accumulator:
    val: int = field(init=False, default=0)
    inst_pos: int = field(init=False, default=0)
    is_loop: bool = field(init=False, default=False)
    is_terminated: bool = field(init=False, default=False)
    program: List[Instruction] = field(repr=False)
    execution_counter: Dict[int, int] = field(repr=False)
    p_length: int

    def __init__(self, program: List[Instruction]) -> None:
        self.all_ops: Dict[str, Callable] = {
            "nop": self.__nop,
            "acc": self.__acc,
            "jmp": self.__jmp,
        }
        self.program = program
        self.execution_counter = {i: 0 for i in range(len(program))}
        self.p_length = len(program)

    def run_till_loop_or_terminate(self) -> None:
        while not (self.is_loop or self.is_terminated):
            self._execute()

    def _execute(self) -> None:
        self.execution_counter[self.inst_pos] += 1

        instruction = self.program[self.inst_pos]
        self.all_ops[instruction.operation](instruction.arg)

        if self.inst_pos >= self.p_length:
            self.is_terminated = True
            return
        if self.execution_counter[self.inst_pos] > 0:
            self.is_loop = True

    def __nop(self, _: int) -> None:
        self.inst_pos += 1

    def __acc(self, arg: int) -> None:
        self.val += arg
        self.inst_pos += 1

    def __jmp(self, arg: int) -> None:
        self.inst_pos += arg


def main():
    with open("d8/d8.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    program = [Instruction(line) for line in lines]
    for inst in program:
        if inst.operation in ("nop", "jmp"):
            inst.flip_nop_jmp()
            a = Accumulator(program)
            a.run_till_loop_or_terminate()
            if a.is_terminated:
                print(a.val)
            inst.flip_nop_jmp()


if __name__ == "__main__":
    main()
