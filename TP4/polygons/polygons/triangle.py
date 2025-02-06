from statistics import geometric_mean

from point import Point
from segment import Segment
from geometry_utils import GeometryUtils

class Triangle:
    """Représente un triangle défini par trois points."""

    def __init__(self, p1: Point, p2: Point, p3: Point):
        """Initialise un triangle avec trois points.

        Un triangle est défini par trois points. Une exception est levée si les trois
        points sont alignés.

        Parameters
        ----------
        p1 : Point
            Premier point du triangle.
        p2 : Point
            Deuxième point du triangle.
        p3 : Point
            Troisième point du triangle.
        """
        if GeometryUtils().are_collinear(p1, p2, p3):
            raise ValueError("Les trois points sont alignés, ce n'est pas un triangle.")
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self) -> float:
        """Calcule le périmètre du triangle.

        Returns
        -------
        float
            Périmètre du triangle.
        """
        return (
                Segment(self.p1, self.p2).length() +
                Segment(self.p2, self.p3).length() +
                Segment(self.p3, self.p1).length()
        )

    def area(self) -> float:
        """Calcule l'aire du triangle.

        Returns
        -------
        float
            Aire du triangle.
        """
        return abs(
            (self.p1.x * (self.p2.y - self.p3.y) +
             self.p2.x * (self.p3.y - self.p1.y) +
             self.p3.x * (self.p1.y - self.p2.y)) / 2
        )

    def __repr__(self):
        """Représentation de l'objet sous forme de chaîne de caractères."""
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"