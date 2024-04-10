def read_input_data() -> str:
    with open('tests/day_01/data.txt') as f:
        return f.read()


def split_by_elf(input: str) -> list[str]:
    input = input.strip()
    if not input:
        return []
    return input.strip().split(sep="\n\n")


def most_calories_carried_by_elf(input: str) -> int:
    by_elf = split_by_elf(input)
    total_calories_by_elf = [sum(int(x) for x in elf.splitlines()) for elf in by_elf]
    return max(total_calories_by_elf)
