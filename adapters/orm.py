from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry, relationship

from domain.model import Book, Author

mapper_registry = registry()

book_table = Table(
    "book",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String),
    Column("year", Integer),
    Column("author_id", Integer, ForeignKey("author.id"), default=None )
)

author_table = Table(
    "author",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String),
    Column("last_name", String),
)
def start_mappers():
    mapper_registry.map_imperatively(
        Book,
        book_table,
        properties={
            "_author": relationship(
                Author
            )
        }
    )

    mapper_registry.map_imperatively(
        Author,
        author_table,
        properties={
            "_books": relationship(
                Book, 
                collection_class=set,),
        },
        
    )