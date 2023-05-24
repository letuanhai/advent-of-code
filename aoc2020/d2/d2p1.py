from dataclasses import dataclass
from typing import Iterator


def find_all_substr(text: str, substr: str) -> Iterator[int]:
    i: int = text.find(substr)
    while i != -1:
        yield i
        i = text.find(substr, i + 1)


@dataclass
class PasswordPolicy:
    min_num_of_char: int
    max_num_of_char: int
    required_char: str


@dataclass
class PasswordLine:
    policy: PasswordPolicy
    password: str

    def validate_pw_line(self) -> bool:
        required_char_in_pw = len(
            list(find_all_substr(self.password, self.policy.required_char))
        )
        return (
            self.policy.min_num_of_char
            <= required_char_in_pw
            <= self.policy.max_num_of_char
        )


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
