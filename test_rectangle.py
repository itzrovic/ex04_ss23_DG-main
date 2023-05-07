import unittest

from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.sut1 = Rectangle(5, 10)
        self.sut2 = Rectangle(23, 17)

    def test_calc_area(self):
        self.assertEqual(30, self.sut1.calc_perimeter())
        self.assertEqual(80, self.sut2.calc_perimeter())


if __name__ == '__main__':
    unittest.main()
