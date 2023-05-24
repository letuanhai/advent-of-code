from dataclasses import dataclass
from typing import Iterator


def find_all_substr(text: str, substr: str) -> Iterator[int]:
    i: int = text.find(substr)
    while i != -1:
        yield i
        i = text.find(substr, i + 1)


@dataclass
class PasswordPolicy:
    first_pos: int
    second_pos: int
    required_char: str


@dataclass
class PasswordLine:
    policy: PasswordPolicy
    password: str

    def validate_pw_line(self) -> bool:
        first_position = (
            self.password[self.policy.first_pos - 1] == self.policy.required_char
        ) and (self.password[self.policy.second_pos - 1] != self.policy.required_char)
        second_position = (
            self.password[self.policy.first_pos - 1] != self.policy.required_char
        ) and (self.password[self.policy.second_pos - 1] == self.policy.required_char)
        return first_position or second_position


def parse_pw_line(pw_line: str) -> PasswordLine:
    """turn pw line: '3-7 g: gdgtnfggq' into PasswordLine instance"""
    splits = pw_line.split(": ")
    policy_parts = splits[0].split(" ")
    required_num_of_char = [int(num) for num in policy_parts[0].split("-")]
    pw_policy = PasswordPolicy(
        required_num_of_char[0], required_num_of_char[1], policy_parts[1]
    )
    return PasswordLine(pw_policy, splits[1])


def main():
    with open("./d2.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    all_pw_lines = [parse_pw_line(line) for line in lines]
    validation_result = [pw_line.validate_pw_line() for pw_line in all_pw_lines]
    print(sum(validation_result))


if __name__ == "__main__":
    main()
