import json
import uuid

from models.product import Product
from db.db_connect import session_maker


def save_to_db(product: dict) -> None:
    with session_maker() as session:
        session.add(Product(
            id=uuid.uuid4(),
            name=product["name"],
            price=product["price"],
            rating=product["rating"],
            reviews=product["reviews"],
            category=product["category"],
        ))
        session.commit()


def save_to_json(product: dict, path: str = 'export/product.json') -> None:
    with open(path, 'w', encoding="utf8") as f:
        json.dump(product, f, ensure_ascii=False)
