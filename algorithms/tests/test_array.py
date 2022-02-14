import unittest

from algorithms.arrays import delete_nth, delete_nth_naive
from algorithms.arrays import flatten, flatten_iter
from algorithms.arrays import garage
from algorithms.arrays import josephus
from algorithms.arrays import limit
from algorithms.arrays import longest_non_repeat_str
from algorithms.arrays import max_ones_index
from algorithms.arrays import Interval, merge_intervals
from algorithms.arrays import missing_ranges


class TestDeleteNth(unittest.TestCase):
    def test_delete_nth_naive(self):
        self.assertListEqual(delete_nth_naive(
            [1, 2, 3, 1, 2, 3], n=1),
            [1, 2, 3])

        self.assertListEqual(delete_nth_naive(
            [1, 2, 3, 1, 2, 3, 3], n=2),
            [1, 2, 3, 1, 2, 3])

        self.assertListEqual(delete_nth_naive(
            [1, 2, 3, 1, 2, 3, 3], n=3),
            [1, 2, 3, 1, 2, 3, 3])

        self.assertListEqual(delete_nth_naive(
            [1, 2, 3, 1, 2, 3, 3], n=0),
            [])

        self.assertListEqual(delete_nth_naive(
            [], n=3),
            [])

    def test_delete_nth(self):
        self.assertListEqual(delete_nth(
            [1, 2, 3, 1, 2, 3], n=1),
            [1, 2, 3])

        self.assertListEqual(delete_nth(
            [1, 2, 3, 1, 2, 3, 3], n=2),
            [1, 2, 3, 1, 2, 3])

        self.assertListEqual(delete_nth(
            [1, 2, 3, 1, 2, 3, 3], n=3),
            [1, 2, 3, 1, 2, 3, 3])

        self.assertListEqual(delete_nth(
            [1, 2, 3, 1, 2, 3, 3], n=0),
            [])

        self.assertListEqual(delete_nth(
            [], n=3),
            [])


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertListEqual(flatten(
            [1, 2, 3, [4, 5], (6, 7, 8), "9"]),
            [1, 2, 3, 4, 5, 6, 7, 8, "9"]
        )

        self.assertListEqual(flatten(
            [1, 2, 3, 4, 5, 6, 7, 8, "9"]),
            [1, 2, 3, 4, 5, 6, 7, 8, "9"]
        )

        self.assertListEqual(flatten(
            [[1, 2, 3, 4, 5, 6, 7, 8, "9"]]),
            [1, 2, 3, 4, 5, 6, 7, 8, "9"]
        )

    def test_flatten_iter(self):
        self.assertListEqual(list(flatten_iter(
            [1, 2, 3, [4, 5], (6, 7, 8), "9"])),
            [1, 2, 3, 4, 5, 6, 7, 8, "9"]
        )

        self.assertListEqual(list(flatten_iter(
            [1, 2, 3, 4, 5, 6, 7, 8, "9"])),
            [1, 2, 3, 4, 5, 6, 7, 8, "9"]
        )

        self.assertListEqual(list(flatten_iter(
            [[1, 2, 3, 4, 5, 6, 7, 8, "9"]])),
            [1, 2, 3, 4, 5, 6, 7, 8, "9"]
        )


class TestGarage(unittest.TestCase):
    def test_garage(self):
        initial = [1, 2, 3, 0, 4]
        final = [0, 3, 2, 1, 4]
        steps, seqs = garage(initial, final)
        self.assertEqual(steps, 4)
        self.assertListEqual(seqs, [
            [0, 2, 3, 1, 4],
            [2, 0, 3, 1, 4],
            [2, 3, 0, 1, 4],
            [0, 3, 2, 1, 4]
        ])


class TestJosephus(unittest.TestCase):
    def test_josephus(self):
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        skip = 3
        self.assertListEqual(list(josephus(int_list, skip)),
                             [3, 6, 9, 4, 8, 5, 2, 7, 1])

        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        skip = 1
        self.assertListEqual(list(josephus(int_list, skip)),
                             [1, 2, 3, 4, 5, 6, 7, 8, 9])

        int_list = []
        skip = 1
        self.assertListEqual(list(josephus(int_list, skip)),
                             [])


class TestLimit(unittest.TestCase):
    def test_limit(self):
        int_list = [1, 2, 3, 4, 5]
        self.assertListEqual(list(limit(int_list)),
                             [1, 2, 3, 4, 5])

        self.assertListEqual(list(limit(int_list, min_lim=2)),
                             [3, 4, 5])

        self.assertListEqual(list(limit(int_list, max_lim=3)),
                             [1, 2])

        self.assertListEqual(list(limit(int_list, min_lim=2, max_lim=3)),
                             [])


class TestLongestNonRepeatStr(unittest.TestCase):
    def test_longest_non_repeat_str(self):
        s = "abcabcbb"
        self.assertEqual(longest_non_repeat_str(s), (3, 'abc'))

        s = "bbbb"
        self.assertEqual(longest_non_repeat_str(s), (1, 'b'))

        s = "pwwkew"
        self.assertEqual(longest_non_repeat_str(s), (3, 'wke'))


class TestMaxOnesIndex(unittest.TestCase):
    def test_max_ones_index(self):
        l = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        self.assertEqual(max_ones_index(l), 3)

        l = [1, 1, 1]
        self.assertEqual(max_ones_index(l), -1)

        l = [0, 0, 0]
        self.assertEqual(max_ones_index(l), 0)

        l = [1, 1, 0]
        self.assertEqual(max_ones_index(l), 2)

        l = [0, 1, 1]
        self.assertEqual(max_ones_index(l), 0)


class TestMergeInterval(unittest.TestCase):
    def test_merge(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        intervals = [Interval(i[0], i[1]) for i in interval_list]
        merged_intervals = Interval.merge(intervals)
        self.assertEqual(merged_intervals,
                         [Interval(1, 6), Interval(8, 10), Interval(15, 18)])

    def test_merge_intervals(self):
        interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
        merged_intervals = merge_intervals(interval_list)
        self.assertEqual(merged_intervals,
                         [[1, 6], [8, 10], [15, 18]])


class TestMissingRanges(unittest.TestCase):
    def test_missing_ranges(self):
        arr = [3, 5, 10, 11, 12, 15, 19]
        self.assertListEqual(missing_ranges(arr, 0, 20),
                             [(0, 2), (4, 4), (6, 9),
                              (13, 14), (16, 18), (20, 20)])
        self.assertListEqual(missing_ranges(arr, 6, 100),
                             [(6, 9), (13, 14), (16, 18), (20, 100)])
