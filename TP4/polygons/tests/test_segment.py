import unittest
from polygons.polygons.point import Point
from polygons.polygons.segment import Segment


class TestSegment(unittest.TestCase):

    def test_segment_length(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        s = Segment(p1, p2)
        self.assertAlmostEqual(s.length(), 5.0)

    def test_invalid_segment(self):
        p1 = Point(1, 1)
        with self.assertRaises(ValueError):
            Segment(p1, p1)

if __name__ == "__main__":
    unittest.main()
