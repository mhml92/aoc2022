import pytest

from aoc2022.day_01.calorie_counting import split_by_elf


@pytest.fixture
def input_data() -> str:
    with open('tests/day_01/data.txt') as f:
        return f.read()


def test_read_input_data(input_data: str):
    assert isinstance(input_data, str)


def test_split_by_elf(input_data: str):
    assert split_by_elf("") == []
    assert split_by_elf("1") == [[1]]
    #assert split_by_elf("1\n1") == [[1, 1]]
    #assert split_by_elf("1\n\n1") == [[1], [1]]
    #assert split_by_elf("1\n1\n\n2") == [[1, 1], [2]]
    #assert split_by_elf("1\n1\n\n2\n\n") == [[1, 1], [2]]

    #assert len(split_by_elf(input_data)) == 5

# def test_most_calories_carried_by_elf(input_data: str):
#    assert most_calories_carried_by_elf("1") == 1
#    assert most_calories_carried_by_elf("1\n\n2") == 2
#    assert most_calories_carried_by_elf("1\n2\n\n2") == 3
#    assert most_calories_carried_by_elf(input_data) == 24000
#
#
# def sum_calories_of_n_most_carrying_elfs(n: int, elfs: list[str]) -> int:
#    return total_calories_by_elf_asc(elfs)[0]
#
#
# def test_sum_n_most_carrying_elfs():
#    assert sum_calories_of_n_most_carrying_elfs(1, ["1"]) == 1
#    assert sum_calories_of_n_most_carrying_elfs(2, ["1"]) == 1
#
#
# def sum_of_top_three_elf_carrying_load(input: str) -> int:
#    return total_calories_by_elf_asc(input)[0]
#
#
# def test_sum_of_top_three_elf_carrying_load():
#    assert sum_of_top_three_elf_carrying_load("1") == 1
