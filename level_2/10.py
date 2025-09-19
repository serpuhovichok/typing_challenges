from constants import ___
import dataclasses


@dataclasses.dataclass(kw_only=True, frozen=True)
class Point:
    x: int
    y: int


def is_point_in_square(point: Point, left_upper_corner: Point, right_bottom_corner: Point) -> bool:
    pass


if __name__ == "__main__":
    assert is_point_in_square(
        point=Point(x=10, y=12),
        left_upper_corner=Point(x=5, y=5),
        right_bottom_corner=Point(x=20, y=15)
    ) is True
