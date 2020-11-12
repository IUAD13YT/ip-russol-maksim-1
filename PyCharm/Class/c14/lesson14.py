# import unittest
#
# """
# assert sum([1, 2, 3]) == 6, 'Should be 6'
# assert sum([1, 1, 1]) == 6, 'Should be 6'
# """
# """
# Traceback (most recent call last):
#   File "/home/dl-academy/PycharmProjects/ip-russol-maksim-1/Class/c14/lesson14.py", line 4, in <module>
#     assert sum([1, 1, 1]) == 6, 'Should be 6'
# AssertionError: Should be 6"""
#
# """МОДУЛЬ UNITTEST"""
#
#
# class TestSum(unittest.TestCase):
#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, 'Should be 6')
#
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 4)), 6, 'Should be 6')
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# def sum(array: list):
#     assert isinstance(array, list) or isinstance(array, tuple)
#     total = 0
#     for val in array:
#         assert isinstance(val, int)
#         total += val
#     return total
#
# sum(3)
# sum([3, 3])
# sum('3333')
# sum(['3', '3'])


def third(x):
    """
    >>> third(6.9)
    2.3000000000000003
    >>>
    """
    return x / 3


if __name__ == '__main__':
    import doctest
    doctest.testmod()