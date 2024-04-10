def read_input_data(path: str) -> str:
    with open(path) as f:
        return f.read()


def split_by_elf(input: str) -> list[str]:
    input = input.strip()
    if not input:
        return []
    return input.split(sep="\n\n")


def total_calories_by_elf(input: list[str]) -> list[int]:
    return [sum(int(x) for x in elf.splitlines()) for elf in input]


def most_calories_carried_by_elf(input: str) -> int:
    by_elf = split_by_elf(input)
    return sorted(total_calories_by_elf(by_elf))[-1]


if __name__ == '__main__':
    input = read_input_data("input.txt")
    print(most_calories_carried_by_elf(input))
