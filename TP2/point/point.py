#!/usr/bin/env python

from math import atan2, cos, sin, sqrt


class Point:
    def __init__(self, x, y):
        """Construit un point

        Parameters
        ----------
        x : float
            abscisse du point
        y : float
            ordonnée du point
        """
        self.__x = x
        self.__y = y

    def __str__(self):
        """Représentation textuelle du point

        Returns
        -------
        str
            description du point
        """
        return f"({self.__x}, {self.__y})"

    @property
    def x(self):
        """Abscisse du point.

        Returns
        -------
        float
            Abscisse du point
        """
        return self.__x

    @property
    def y(self):
        """Ordonnée du point.

        Returns
        -------
        float
            Ordonnée du point
        """
        return self.__y

    @property
    def r(self):
        """Distance en coordonnées polaires.

        Returns
        -------
        float
            Distance r à l'origine
        """
        return sqrt(self.__x**2 + self.__y**2)

    @property
    def t(self):
        """Angle en coordonnées polaires

        Returns
        -------
        float
            angle avec l'axe des abscisses
        """
        return atan2(self.__y, self.__x)

    def __eq__(self, other):
        """Teste l'égalité de deux points

        Parameters
        ----------
        other : Point
            Autre point à tester

        Returns
        -------
        bool
            True si et seulement si les coordonnées correspondent
        """
        return self.__x == other.__x and self.__y == other.__y

    def __add__(self, other):
        """Additionne deux points

        Parameters
        ----------
        other : Point
            Autre point à ajouter

        Returns
        -------
        Point
            Nouveau point résultant de l'addition
        """
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        """Soustrait deux points

        Parameters
        ----------
        other : Point
            Autre point à soustraire

        Returns
        -------
        Point
            Nouveau point résultant de la soustraction
        """
        return Point(self.__x - other.__x, self.__y - other.__y)

    def homothety(self, k):
        """Applique un homothétie au point

        Parameters
        ----------
        k : float
            le rapport d'homothétie à appliquer
        """
        self.__x *= k
        self.__y *= k

    def translation(self, dx, dy):
        """Applique une translation

        Parameters
        ----------
        dx : float
            la translation selon l'axe horizontal
        dy : float
            la translation selon l'axe vertical
        """
        self.__x += dx
        self.__y += dy

    def rotation(self, a):
        """Applique une rotation par rapport à l'origine

        Parameters
        ----------
        a : float
            l'angle de rotation
        """
        r = self.r
        t = self.t + a
        self.__x = r * cos(t)
        self.__y = r * sin(t)