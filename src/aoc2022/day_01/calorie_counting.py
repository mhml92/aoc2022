def read_input_data(path: str) -> str:
    with open(path) as f:
        return f.read()


def split_by_elf(input: str) -> list[str]:
    input = input.strip()
    if not input:
        return []
    return input.split(sep="\n\n")


def most_calories_carried_by_elf(input: str) -> int:
    by_elf = split_by_elf(input)
    total_calories_by_elf = sorted([sum(int(x) for x in elf.splitlines()) for elf in by_elf])
    return total_calories_by_elf[-1]


if __name__ == '__main__':
    input = read_input_data("input.txt")
    print(most_calories_carried_by_elf(input))
