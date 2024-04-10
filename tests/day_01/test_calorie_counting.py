def read_test_data() -> list[str]:
    with open('tests/day_01/data.txt') as f:
        return f.read().splitlines()


def test_group_items_by_elf():
    assert isinstance(read_test_data(), list)
