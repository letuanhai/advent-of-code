from typing import Dict, Optional, List
from dataclasses import dataclass

EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


@dataclass(kw_only=True)
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = None

    def is_valid(self) -> bool:
        return self._validate()

    def _validate(self) -> bool:
        byr: bool = 1920 <= int(self.byr) <= 2002
        iyr: bool = 2010 <= int(self.iyr) <= 2020
        eyr: bool = 2020 <= int(self.eyr) <= 2030
        hgt: bool = (
            150 <= int(self.hgt[:-2]) <= 193 if self.hgt.endswith("cm") else False
        ) or (59 <= int(self.hgt[:-2]) <= 76 if self.hgt.endswith("in") else False)
        hcl: bool = (
            len(self.hcl) == 7
            and self.hcl.startswith("#")
            and all(c in "0123456789abcdef" for c in self.hcl[1:])
        )
        ecl: bool = self.ecl in EYE_COLORS
        pid: bool = len(self.pid) == 9 and bool(int(self.pid))
        return byr and iyr and eyr and hgt and hcl and ecl and pid


def parse_pp_dict(pp_line: str) -> Dict:
    pp_dict = {}
    for split_nl in pp_line.split("\n"):
        for split_sp in split_nl.split(" "):
            splits = split_sp.split(":")
            pp_dict[splits[0]] = splits[1]
    return pp_dict


def main():
    with open("d4/d4.txt", "r") as f:
        lines = f.read()

    pp_dicts = [parse_pp_dict(line) for line in lines.split("\n\n")]

    valid_passports: List[Passport] = []
    for p in pp_dicts:
        try:
            passport = Passport(**p)
            if passport.is_valid():
                valid_passports.append(passport)
        except (TypeError, ValueError):
            pass
    print(len(valid_passports))


if __name__ == "__main__":
    main()
