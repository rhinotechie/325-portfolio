import unittest
from GetTesla import getTesla


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        grid_matrix = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
        self.assertEqual(2, getTesla(grid_matrix))

    def test_personal1(self):
        grid_matrix = [[-10]]
        self.assertEqual(11, getTesla(grid_matrix))

    def test_personal2(self):
        grid_matrix = [[10]]
        self.assertEqual(1, getTesla(grid_matrix))

    def test_personal3(self):
        grid_matrix = [[0]]
        self.assertEqual(1, getTesla(grid_matrix))

    def test_personal4(self):
        grid_matrix = [[5, 5, -10]]
        self.assertEqual(1, getTesla(grid_matrix))

    def test_personal5(self):
        grid_matrix = [[-10, 5, -6]]
        self.assertEqual(12, getTesla(grid_matrix))


if __name__ == '__main__':
    unittest.main()
