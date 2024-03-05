from api.extensions import db


class Projects(db.Document):
    num = db.SequenceField(required=True, min_value=1)
    description = db.StringField(required=True)
