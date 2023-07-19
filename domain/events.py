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

#Potentially find place where I can serialize this before placing on queue? 
@dataclass
class BookCreated(Event):
    book_id: str
    author_id: str
