def read_test_data() -> list[str]:
    with open('tests/day_01/data.txt') as f:
        return f.read().splitlines()


def test_read_data_as_list():
    assert isinstance(read_test_data(), list)


def group_by_elf() -> list[list[str]]:
    return [[], [], [], [], []]


def test_group_items_by_elf():
    assert len(group_by_elf()) == 5
