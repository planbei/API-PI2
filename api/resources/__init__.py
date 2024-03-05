from .users import ns as users_routes
from .projects import ns as projects_routes


def add_namespaces(api):
    api.add_namespace(users_routes)
    api.add_namespace(projects_routes)