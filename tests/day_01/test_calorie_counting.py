def read_input_data() -> str:
    with open('tests/day_01/data.txt') as f:
        return f.read()


def test_read_data():
    assert isinstance(read_input_data(), str)


#def group_by_elf() -> list[list[str]]:
#    for
#    return [[], [], [], [], []]
#
#
#def test_group_items_by_elf():
#    assert len(group_by_elf()) == 5
