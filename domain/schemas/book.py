from marshmallow import Schema, fields, validates_schema, ValidationError, post_load

from BookService.domain.model.book import Author, Book

class AuthorSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()

    @post_load
    def make_author(self, data, **kwargs):
        return Author(**data)

class BookSchema(Schema):
    #author = fields.Str()
    id = fields.Int()
    title = fields.Str(required=True)
    year = fields.Int()

    #TODO: Determine if I can allow author_id to share the id field of AuthorSchema.
    
    author_id = fields.Int(required=False)
    #author = fields.Nested(AuthorSchema, required=False)
    #author = fields.Str()

    # @validates_schemaå
    # def validate_author_fields(self, data, **kwargs):
    #     if not data.get("author_id") and not data.get("author"):
    #         raise ValidationError("Either 'author_id' or 'author' is required.")
    #     if data.get("author_id") and data.get("author"):
    #         raise ValidationError("Only one of 'author_id' or 'author' fields can be set")
        
    # class Meta:
    #     exclude = ("author",)

    @post_load
    def make_book(self, data, **kwargs):
        return Book(**data)
    
#TODO: Determine if this is too much 'business logic' in my schema
#TODO: Problem: This is breaking single responsibility principle, because it is both doing deserialization, and 
#conversion to sqlalchemy object. Hm. 