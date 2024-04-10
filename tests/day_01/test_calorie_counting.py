def read_test_data() -> str:
    with open('tests/day_01/data.txt') as f:
        return f.read()


def test_read_list():
    assert read_test_data()
