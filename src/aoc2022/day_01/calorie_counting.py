def read_input_data(path: str) -> str:
    with open(path) as f:
        return f.read()


def split_by_elf(input: str) -> list[list[int]]:
    input = input.strip()
    if not input:
        return []
    try:
        x = int(input)
        return [[x]]
    except:
        pass

    return [[int(x) for x in s.splitlines()] for s in input.split(sep="\n\n")]


def total_calories_by_elf_asc(input: list[str]) -> list[int]:
    return sorted([sum(int(x) for x in elf.splitlines()) for elf in input])


def most_calories_carried_by_elf(input: str) -> int:
    by_elf = split_by_elf(input)
    return total_calories_by_elf_asc(by_elf)[-1]


if __name__ == '__main__':
    input = read_input_data("input.txt")
    print(most_calories_carried_by_elf(input))
