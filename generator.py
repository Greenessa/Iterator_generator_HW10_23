import types
def flat_list_gen(some_list):
    list_new = []
    for l in some_list:
        if isinstance(l, list):
            yield from flat_list_gen(l)
        else:
            yield l

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_list_gen(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_list_gen(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_list_gen(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

