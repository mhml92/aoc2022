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


def total_calories_by_elf_asc(input: list[Elf]) -> list[int]:
    return sorted([elf.calories_carried() for elf in input])


def most_calories_carried_by_elf(input: str) -> int:
    by_elf = split_by_elf(input)
    return total_calories_by_elf_asc(by_elf)[-1]


if __name__ == '__main__':
    input = read_input_data("input.txt")
    print(most_calories_carried_by_elf(input))
