import math
from point import Point

class Segment:
    """Représente un segment entre deux points."""

    def __init__(self, p1: Point, p2: Point):
        """
        Constructeur d'un segment.

        Parameters
        ----------
        p1 : Point
            Le premier point du segment.
        p2 : Point
            Le deuxième point du segment.
        """
        if p1.x == p2.x and p1.y == p2.y:
            raise ValueError("Un segment doit avoir deux points distincts.")
        self.p1 = p1
        self.p2 = p2

    def length(self) -> float:
        """Calcule la longueur du segment.

        Returns
        -------
        float
            La longueur du segment.
        """
        return math.sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)

    def __repr__(self):
        """Représentation d'un segment."""e
        return f"Segment({self.p1}, {self.p2})"