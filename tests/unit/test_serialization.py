import json
from domain.model import Book, Author

def test_book_can_serialize():
    author = Author(
        first_name="John",
        last_name="Steinbeck"
    )
    book = Book(
        title="Grapes of Wrath",
        year=1937,
        author=author
    )

    print(book.__json__())
    print(json.dumps(book.__json__()))