from aoc2022.day_01.calorie_counting import split_by_elf, most_calories_carried_by_elf


def read_test_input_data() -> str:
    with open('tests/day_01/data.txt') as f:
        return f.read()


def test_read_input_data():
    assert isinstance(read_test_input_data(), str)


def test_most_calories_carried_by_elf():
    assert most_calories_carried_by_elf("1") == 1
    assert most_calories_carried_by_elf("1\n\n2") == 2
    assert most_calories_carried_by_elf("1\n2\n\n2") == 3
    assert most_calories_carried_by_elf(read_test_input_data()) == 24000


def test_split_by_elf():
    assert split_by_elf("") == []
    assert split_by_elf("1") == ["1"]
    assert split_by_elf("1\n1") == ["1\n1"]
    assert split_by_elf("1\n\n1") == ["1", "1"]
    assert split_by_elf("1\n1\n\n2") == ["1\n1", "2"]
    assert split_by_elf("1\n1\n\n2\n\n") == ["1\n1", "2"]

    assert len(split_by_elf(read_test_input_data())) == 5
