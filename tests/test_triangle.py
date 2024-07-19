import math

import pytest

from shapetools import Triangle


@pytest.mark.parametrize(
    "sides",
    (
        (0, 0, 1),
        (-1, 2, 3),
        (10, 2, 3),
    ),
)
def test_triangle_error(sides: tuple[float, float, float]) -> None:
    with pytest.raises(ValueError):
        Triangle(*sides)


@pytest.mark.parametrize(
    "sides, area",
    (
        ((1, 1, 2), 0),
        ((3, 4, 5), 6),
        ((6, 6, 6), 9 * math.sqrt(3)),
    ),
)
def test_triangle_area(sides: tuple[float, float, float], area: float) -> None:
    t = Triangle(*sides)
    assert t.area() == pytest.approx(area)


@pytest.mark.parametrize(
    "sides, is_right",
    (
        ((3, 4, 5), True),
        ((1, 1, 1), False),
    ),
)
def test_triangle_is_right(sides: tuple[float, float, float], is_right: bool) -> None:
    t = Triangle(*sides)
    assert t.is_right == is_right
