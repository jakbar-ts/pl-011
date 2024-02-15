from marshmallow import Schema, fields

class StudentSchema(Schema):
    id = fields.Int(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    date_of_birth = fields.Date(required=True)

def serialize_student(student_data):
    schema = StudentSchema()
    result = schema.dump(student_data)
    return result
