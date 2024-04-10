def read_input_data() -> str:
    with open('tests/day_01/data.txt') as f:
        return f.read()


def test_read_input_data():
    assert isinstance(read_input_data(), str)


def group_by_elf(input: str) -> list[str]:
    input = input.strip()
    if not input:
        return []
    return input.strip().split(sep="\n\n")


def test_group_items_by_elf():
    assert group_by_elf("") == []
    assert group_by_elf("1") == ["1"]
    assert group_by_elf("1\n1") == ["1\n1"]
    assert group_by_elf("1\n\n1") == ["1", "1"]
    assert group_by_elf("1\n1\n\n2") == ["1\n1", "2"]
    assert group_by_elf("1\n1\n\n2\n\n") == ["1\n1", "2"]

    assert len(group_by_elf(read_input_data())) == 5

