import pytest

from aoc2022.day_01.calorie_counting import split_by_elf, Elf, most_calories_carried_by_elf, total_calories_by_elf_desc


@pytest.fixture
def input_data() -> str:
    with open('tests/day_01/data.txt') as f:
        return f.read()


def test_read_input_data(input_data: str):
    assert isinstance(input_data, str)


def test_split_by_elf(input_data: str):
    assert split_by_elf("") == []
    assert split_by_elf("1") == [Elf(calories=[1])]
    assert split_by_elf("1\n1") == [Elf(calories=[1, 1])]
    assert split_by_elf("1\n\n1") == [Elf(calories=[1]), Elf(calories=[1])]
    assert split_by_elf("1\n1\n\n2") == [Elf(calories=[1, 1]), Elf(calories=[2])]
    assert split_by_elf("1\n1\n\n2\n\n") == [Elf(calories=[1, 1]), Elf(calories=[2])]

    assert len(split_by_elf(input_data)) == 5


def test_most_calories_carried_by_elf(input_data: str):
    assert most_calories_carried_by_elf("1") == 1
    assert most_calories_carried_by_elf("1\n\n2") == 2
    assert most_calories_carried_by_elf("1\n2\n\n2") == 3
    assert most_calories_carried_by_elf(input_data) == 24000


def sum_calories_of_n_most_carrying_elfs(n: int, elfs: list[Elf]) -> int:
    totals = total_calories_by_elf_desc(elfs)
    return sum(totals[:min(len(totals), n)])


def test_sum_n_most_carrying_elfs():
    assert sum_calories_of_n_most_carrying_elfs(1, [Elf(calories=[1])]) == 1


def sum_of_top_three_elf_carrying_load(input: str) -> int:
    elfs = split_by_elf(input)
    return sum_calories_of_n_most_carrying_elfs(3, elfs)


def test_sum_of_top_three_elf_carrying_load(input_data):
    assert sum_of_top_three_elf_carrying_load("1") == 1
    assert sum_of_top_three_elf_carrying_load("1\n\n1") == 2
    assert sum_of_top_three_elf_carrying_load(input_data) == 45000
