import unittest

from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.sut1 = Rectangle(5, 10)
        self.sut2 = Rectangle(23, 17)

    def test_calc_area(self):
        self.assertEqual(50, self.sut1.calc_area())
        self.assertEqual(391, self.sut2.calc_area())

    def test_calc_perimeter(self):
        self.assertEqual(30, self.sut1.calc_perimeter())
        self.assertEqual(80, self.sut2.calc_perimeter())

    # imported from README
    def test_equal_rectangle(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(4, 3)
        r3 = Rectangle(3, 4)

        self.assertEqual(r1, r3)
        self.assertNotEqual(r1, r2)

    def test_hash_rectangle(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(4, 3)
        r3 = Rectangle(3, 4)

        self.assertEqual(hash(r1), hash(r3))
        self.assertNotEqual(hash(r1), hash(r2))


if __name__ == '__main__':
    unittest.main()
