import re


with open("input/day04.txt") as puzzle_input:
    raw = puzzle_input.read().split("\n\n")
    passports = [dict(re.findall("([a-z]+):([a-z0-9#]+)", p)) for p in raw]

required_fields = {
    "byr": [(r"(\d{4})", lambda x: 1920 <= int(x) <= 2002)],
    "iyr": [(r"(\d{4})", lambda x: 2010 <= int(x) <= 2020)],
    "eyr": [(r"(\d{4})", lambda x: 2020 <= int(x) <= 2030)],
    "hgt": [
        (r"(\d+)cm", lambda x: 150 <= int(x) <= 193),
        (r"(\d+)in", lambda x: 59 <= int(x) <= 76),
    ],
    "hcl": [(r"#[a-f0-9]{6}",)],
    "ecl": [(r"(amb|blu|brn|gry|grn|hzl|oth)",)],
    "pid": [(r"\d{9}",)],
}


def _check_validator(value, validator):
    try:
        value = re.fullmatch(validator[0], value)
        if not value:
            return False

        if len(validator) == 2:
            return validator[1](value.groups()[0])
        return True
    except KeyError:
        return False


def _is_valid(passport):
    for key, validators in required_fields.items():
        try:
            valid = any(_check_validator(passport[key], v) for v in validators)
            if not valid:
                return False
        except KeyError:
            return False
    return True


def part_1():
    return sum(
        1 if len(p) == 8 or (len(p) == 7 and "cid" not in p) else 0 for p in passports
    )


def part_2():
    return sum(1 if _is_valid(p) else 0 for p in passports)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
