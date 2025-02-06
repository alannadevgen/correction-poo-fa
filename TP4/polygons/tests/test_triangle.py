import unittest
from polygons.polygons.point import Point
from polygons.polygons.triangle import Triangle
from polygons.polygons.segment import Segment


class TestTriangle(unittest.TestCase):

    def test_triangle_perimeter(self):
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        p3 = Point(0, 4)
        t = Triangle(p1, p2, p3)
        self.assertAlmostEqual(t.perimeter(), 12.0)

    def test_invalid_triangle(self):
        # Les points sont alignés
        p1 = Point(0, 0)
        p2 = Point(1, 1)
        p3 = Point(2, 2)
        with self.assertRaises(ValueError):
            Triangle(p1, p2, p3)

if __name__ == "__main__":
    unittest.main()
