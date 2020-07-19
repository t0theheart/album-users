from marshmallow import fields, Schema


class LoginResponse(Schema):
    login = fields.String(required=True, description='User login', example='Ivan')
