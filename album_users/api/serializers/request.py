from marshmallow import fields, Schema


class LoginRequest(Schema):
    login = fields.String(required=True, description='User login', example='Ivan')
    password = fields.String(required=True, description='User password', example='ivan12345')
