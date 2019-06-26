import unittest

from point import *


class TestPoint(unittest.TestCase):
    def test01_test_init(self):
        p = Point(1, 2)

        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test02_test_eq(self):
        p = Point(1, 2)
        q = Point(1, 2)

        self.assertEqual(p, q)

    def test03_test_neq(self):
        p = Point(1, 2)
        q = Point(2, 1)

        self.assertNotEqual(p, q)
        self.assertNotEqual(p, "(1, 2)")

    def test04_test_repr(self):
        p = Point(1, 2)

        self.assertEqual(repr(p), "Point(1, 2)")

    def test05_test_translate(self):
        p1 = Point(1, 2)
        p2 = translate(p1, 1, 1)

        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 2)
        self.assertEqual(p2.x, 2)
        self.assertEqual(p2.y, 3)


if __name__ == "__main__":
    unittest.main()
