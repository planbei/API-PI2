from flask_restx import fields
from api.extensions import api

project_model = api.model("Project", {
    "num": fields.Integer,
    "description": fields.String
})

project_input_model = api.model("ProjectInput", {
    "description": fields.String
})