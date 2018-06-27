import unittest
from src.demo import Demo

class TPopulationCount(unittest.TestCase):

    def setUp(self):
        #print("[setUp]")
        self.d = Demo()

    def tearDown(self):
        #print("[tearDown]")
        pass

    def test_population_count_1(self):
        res = self.d.population_count(0)
        self.assertEqual(res, 0)

    def test_population_count_2(self):
        res = self.d.population_count(8)
        self.assertEqual(res, 1)

    def test_population_count_3(self):
        res = self.d.population_count(15)
        self.assertEqual(res, 4)

    def test_population_count_4(self):
        res = self.d.population_count(19)
        self.assertEqual(res, 3)


class TLargestSubArray(unittest.TestCase):

    def setUp(self):
        #print("[setUp]")
        self.d = Demo()

    def tearDown(self):
        #print("[tearDown]")
        pass

    def test_largest_subarray_1(self):
        res = self.d.largest_subarray([1, 2, 4])
        self.assertEqual(res, 7)

    def test_largest_subarray_2(self):
        res = self.d.largest_subarray([-21, -1, -1, 0])
        self.assertEqual(res, 0)

    def test_largest_subarray_3(self):
        res = self.d.largest_subarray([1, 2, -10, 3, 100, 1222])
        self.assertEqual(res, 1325)

    def test_largest_subarray_4(self):
        res = self.d.largest_subarray([-1, -2, -5])
        self.assertEqual(res, -1)

if __name__ == '__main__':
    unittest.main()

