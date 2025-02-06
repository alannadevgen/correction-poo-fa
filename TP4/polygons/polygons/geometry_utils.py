from typing import final
from point import Point

@final
class GeometryUtils:
    """Classe utilitaire (finale) pour la géométrie."""

    @staticmethod
    def are_collinear(p1: Point, p2: Point, p3: Point) -> bool:
        """Vérifie si trois points sont alignés."""
        return (p2.x - p1.x) * (p3.y - p1.y) == (p3.x - p1.x) * (p2.y - p1.y)