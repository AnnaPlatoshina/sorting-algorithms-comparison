import unittest
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 3, 8, 6, 7, 2], [2, 3, 5, 6, 7, 8]),
            ([-1, -2, -3], [-3, -2, -1])
        ]

    def test_bubble_sort(self):
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr, expected=expected):
                self.assertEqual(bubble_sort(input_arr.copy()), expected)

    def test_selection_sort(self):
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr, expected=expected):
                self.assertEqual(selection_sort(input_arr.copy()), expected)

    def test_insertion_sort(self):
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr, expected=expected):
                self.assertEqual(insertion_sort(input_arr.copy()), expected)


if __name__ == '__main__':
    unittest.main()