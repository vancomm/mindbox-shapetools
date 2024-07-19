from __future__ import annotations

import abc
import math
import sys

if sys.version_info < (3, 12):
    import typing_extensions as T
else:
    import typing as T


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float: ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("radius must not be negative")

        self.radius = radius

    @T.override
    def area(self) -> float:
        return math.pi * self.radius**2


class Triangle(Shape):
    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float) -> None:
        if a < 0 or b < 0 or c < 0:
            raise ValueError("side lengths must not be negative")

        if a + b < c or a + c < b or b + c < a:
            raise ValueError(f"side lengths {a}, {b}, {c} cannot produce a triangle")

        self.a = a
        self.b = b
        self.c = c

    @T.override
    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    @property
    def is_right(self) -> bool:
        leg1, leg2, hypot = sorted((self.a, self.b, self.c))
        return hypot**2 == leg1**2 + leg2**2
