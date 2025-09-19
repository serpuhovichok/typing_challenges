from constants import ___
import dataclasses


@dataclasses.dataclass(kw_only=True)
class User:
    name: str
    age: int
    spending: list[int]


def calculate_total_spent_for_user(user: User) -> int:
    pass


if __name__ == "__main__":
    assert calculate_total_spent_for_user(user=User(name="Ilya", age=32, spending=[102, 15, 63, 12])) == 192
