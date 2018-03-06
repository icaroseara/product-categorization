from marshmallow import Schema, fields

class ProductSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
