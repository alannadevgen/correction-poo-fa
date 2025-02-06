import unittest
from polygons.polygons.point import Point


class TestSegment(unittest.TestCase):

    def test_point_valid(self):
        p1 = Point(0, 0)
        p2 = Point(3, 6)
        self.assertAlmostEqual(p1.x, 0)
        self.assertAlmostEqual(p1.y, 0)
        self.assertAlmostEqual(p2.x, 3)
        self.assertAlmostEqual(p2.y, 6)

if __name__ == "__main__":
    unittest.main()
