from marshmallow import Schema, fields

class ProductSchema(Schema):
    name = fields.Str()
    description = fields.Str()
