from point import Point
from math import pi


if __name__ == "__main__":
    # Create points
    p1 = Point(1, 2)
    p2 = Point(2, 6)

    # Display points
    print(p1)
    print(p2)

    # Equality
    print(p1 == p2)

    # Properties
    print(p1.x)
    print(p1.y)
    print(p1.r)
    print(p1.t)

    # Homothety
    p1.homothety(2)
    print(p1)

    # Translation
    p2.translation(1, -1)
    print(p2)

    # Rotation
    p2.rotation(pi/2)
    print(p2)
