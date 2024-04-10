from pydantic import BaseModel


def read_input_data(path: str) -> str:
    with open(path) as f:
        return f.read()


class Elf(BaseModel):
    calories: list[int]

    def calories_carried(self):
        return sum(self.calories)


def split_by_elf(input: str) -> list[Elf]:
    input = input.strip()
    if not input:
        return []
    return [Elf(calories=[int(x) for x in s.splitlines()]) for s in input.split(sep="\n\n")]


def total_calories_by_elf_desc(input: list[Elf]) -> list[int]:
    return sorted([elf.calories_carried() for elf in input], reverse=True)


def most_calories_carried_by_elf(input: str) -> int:
    elfs = split_by_elf(input)
    return sum_calories_of_n_most_carrying_elfs(1, elfs)


def sum_calories_of_n_most_carrying_elfs(n: int, elfs: list[Elf]) -> int:
    totals = total_calories_by_elf_desc(elfs)
    return sum(totals[:min(len(totals), n)])


def sum_of_top_three_elf_carrying_load(input: str) -> int:
    elfs = split_by_elf(input)
    return sum_calories_of_n_most_carrying_elfs(3, elfs)


if __name__ == '__main__':
    input = read_input_data("input.txt")
    print(most_calories_carried_by_elf(input))
