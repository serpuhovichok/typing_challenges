import datetime

from constants import ___
import dataclasses


@dataclasses.dataclass(kw_only=True)
class Product:
    name: str
    amount: int
    price: float


@dataclasses.dataclass(kw_only=True)
class Receipt:
    id: int
    date: datetime.date
    products: list[Product]


def parse_receipt(raw_receipt: str) -> Receipt:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == Receipt(
        id=12,
        date=datetime.date(2022, 6, 12),
        products=[Product(name="Молоко", amount=1, price=32.2)]
    )
