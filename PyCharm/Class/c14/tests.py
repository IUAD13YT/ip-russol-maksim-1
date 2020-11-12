import unittest


# def sum(array: list):
#     total = 0
#     for val in array:
#         total += val
#     return total
#
#
# assert (sum([3, 3])) == 6, 'Должно быть 6'
#
#
# def sum(array: list):
#     total = '0'
#     for val in array:
#         total += val
#     return total
#
#
# assert sum('3333') == '03333', 'Должно быть 03333'
#
#
# def sum(array: list):
#     total = '0'
#     for val in array:
#         total += val
#     return total
#
#
# assert sum(['3', '3']) == '033', 'Должно быть 033'


def sum(array: list):
    assert isinstance(array, list) or isinstance(array, tuple)
    total = 0
    for val in array:
        assert isinstance(val, int)
        total += val
    return total


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = 3
        result = sum(data)
        self.assertIs(result, list, 'Should be list')


if __name__ == '__main__':
    unittest.main()

