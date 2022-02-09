import unittest

from algorithms.arrays import delete_nth, delete_nth_naive
from algorithms.arrays import flatten, flatten_iter
from algorithms.arrays import garage
from algorithms.arrays import josephus
from algorithms.arrays import limit


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
