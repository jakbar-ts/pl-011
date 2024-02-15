from marshmallow import fields, Schema


class ProductSchema(Schema):
    id = fields.UUID( required=True)
    name = fields.Str( required=True)
    price = fields. Float( required=True)


def deserialize_product(json_data):
    pass