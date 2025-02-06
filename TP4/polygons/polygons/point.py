class Point:
    """Représente un point dans le plan."""

    def __init__(self, x: float, y: float):
        """
        Constructeur de la classe Point.

        Parameters
        ----------
        x : float
            Abscisse du point
        y : float
            Ordonnée du point
        """
        self.x = x
        self.y = y

    def __str__(self):
        """Affichage du point sous forme de chaîne de caractères."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Représentation du point sous forme de chaîne de caractères."""
        return f"Point({self.x}, {self.y})"
