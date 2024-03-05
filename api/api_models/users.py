from flask_restx import fields
from api.extensions import api

user_model = api.model("User", {
    "id": fields.String,
    "surname": fields.String,
    "name": fields.String,
    "email": fields.String,
    "company": fields.String,
    "active": fields.Boolean
    #"roles": fields.List
})

user_input_model = api.model("UserInput", {
    "surname": fields.String,
    "name": fields.String,
    "email": fields.String,
    "password": fields.String,
    "company": fields.String
})