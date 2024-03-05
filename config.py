import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir de .env
load_dotenv()

mongo_username = os.getenv('MONGO_USERNAME')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_cluster_name = os.getenv('MONGO_CLUSTER_NAME')
db_name = os.getenv('DB_NAME')
mongo_uri = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster_name.lower()}.w7iabmm.mongodb.net/?retryWrites=true&w=majority&appName="


class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_SECRET = SECRET_KEY
    MONGODB_SETTINGS = {
            'host': mongo_uri,
            'db': db_name
        }

