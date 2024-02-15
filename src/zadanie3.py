from marshmallow import fields, Schema


class ProductSchema(Schema):
    id = fields.UUID(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


def deserialize_product(json_data):
    schema = ProductSchema()
    try:
        deserialized_data = schema.loads(json_data)
        return deserialized_data
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None
