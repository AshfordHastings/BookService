from marshmallow import Schema, fields

class AuthorSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()

class MDataSchema(Schema):
    ext = fields.Str()

class BookSchema(Schema):
    title = fields.Str()
    year = fields.Int()
    author = fields.Nested(AuthorSchema)
    m_data = fields.Nested(MDataSchema)