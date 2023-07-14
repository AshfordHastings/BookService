from dataclasses import dataclass
from domain.model.book import Author

class Event:
    pass

@dataclass
class OutOfStock(Event):
    sku: str

@dataclass
class BookLimitReached(Event):
    user_id: str

