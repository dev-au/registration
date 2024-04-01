from tortoise import fields, Model


class User(Model):
    username = fields.CharField(pk=True, max_length=255)
    fullname = fields.CharField(max_length=255)
    hashed_password = fields.TextField()

