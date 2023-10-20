
class FlatIterator:

    def __init__(self, list_of_list):
        self.flat_list = self.flattener(list_of_list)
        self.cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor +=1
        if self.cursor==len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.cursor]

    def flattener(self, some_list):
        list_new = []
        for l in some_list:
            if isinstance(l, (list, tuple)):
                list_new.extend(self.flattener(l))
            else:
                list_new.append(l)
        return list_new


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()