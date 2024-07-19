import math

import pytest

from shapetools import Circle


@pytest.mark.parametrize(
    "radius",
    (
        -2,
        -0.5,
    ),
)
def test_circle_error(radius: float) -> None:
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    "radius, area",
    (
        (0, 0),
        (1, math.pi),
        (2, 4 * math.pi),
    ),
)
def test_circle_area(radius: float, area: float) -> None:
    assert Circle(radius).area() == pytest.approx(area)
