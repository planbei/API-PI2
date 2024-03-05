from flask import request
from flask_restx import Resource, Namespace
from mongoengine import *
from api.models.users import Users
from api.api_models.users import user_model, user_input_model

ns = Namespace("api")


@ns.route("/users")
class UsersListAPI(Resource):

    @ns.marshal_list_with(user_model)
    def get(self):
        return [user for user in Users.objects]

    @ns.expect(user_input_model)
    @ns.marshal_with(user_model)
    def post(self):
        try:
            user = Users(surname=ns.payload["surname"],
                         name=ns.payload["name"],
                         email=ns.payload["email"],
                         password=ns.payload["password"],
                         company=ns.payload["company"],
                         active=ns.payload["active"])

            user.save()
            return user, 201
        except Exception as e:
            print(f"Error in users[POST] : {str(e)}")


@ns.route("/users/<string:id>")
class UserAPI(Resource):
    @ns.marshal_with(user_model)
    def get(self, id):
        return Users.objects(id=id).first()

    @ns.marshal_with(user_model)
    def put(self, objectId):
        user = Users.objects(id=id).first()

    def delete(self, objectId):
        user = Users.objects(id=id).first()
        user.delete()
        return {"message": "utilisateur supprimé"}, 204
