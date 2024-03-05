from flask_restx import Resource, Namespace
from mongoengine import *
from api.models.projects import Projects
from api.api_models.projects import project_model, project_input_model


ns = Namespace('api')


@ns.route("/projects")
class ProjectListAPI(Resource):

    @ns.marshal_list_with(project_model)
    def get(self):
        return [project for project in Projects.objects]

    @ns.expect(project_input_model)
    @ns.marshal_with(project_model)
    def post(self):
        try:
            project = Projects(description=ns.payload["description"])

            num = Projects.objects()
            project.save()
            return project, 201

        except Exception as e:
            print(f"Error in projects[POST] : {str(e)}")


@ns.route("/projects/<int:num>")
class ProjectAPI(Resource):
    @ns.marshal_with(project_model)
    def get(self, num):
        return Projects.objects(num=num).first()

    @ns.marshal_with(project_model)
    def put(self, num):
        project = Projects.objects(num=num).first()

    def delete(self, num):
        project = Projects.objects(num=num).first()
        project.delete()
        return {"message": "project deleted"}, 204
