from domain.model import Author, Book, BookInfo, BookMetadata
from adapters.orm import AuthorModel, BookModel

def map_author_model_to_entity(instance: AuthorModel) -> Author:
    return Author(
        id=instance.id,
        first_name=instance.first_name,
        last_name=instance.last_name
    )

def map_author_entity_to_model(author: Author, existing=None) -> AuthorModel:
    return AuthorModel(
        id=author.id,
        first_name=author.first_name,
        last_name=author.last_name
    )

def map_book_model_to_entity(instance: BookModel) -> Book:
    def map_to_book_info(instance:BookModel) -> BookInfo:
        return BookInfo(
            title=instance.title,
            year=instance.year,
            author=map_author_model_to_entity(instance.author)
        )
    def map_to_book_metadata(instance:BookModel) -> BookMetadata:
        return BookInfo(
            file_extension=instance.file_extension
        )
    return Book(
        id=instance.id,
        info=map_to_book_info(instance),
        metadata=map_to_book_metadata(instance)
    )

def map_book_entity_to_model(book: Book, existing=None) -> BookModel:
    return BookModel(
        id=book.id,
        title=book.info.title,
        year=book.info.year,
        author=book.info.author,
        file_extension=book.metadata.file_extension
    )


#Consider making this a Mixin...