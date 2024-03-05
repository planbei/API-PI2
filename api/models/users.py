from api.extensions import db

ROLES = ["admin", "company_partner", "student", "teacher", "IF_responsible", "OCC_responsible", "MMN_responsible",
         "EVD_responsible", "ACT_responsible", "FIN_responsible", "DIA_responsible", "IND_responsible",
         "SB_responsible", "CREATECH_responsible", "CCC_responsible", "AFS_responsible"]


class Users(db.Document):
    surname = db.StringField(required=True)
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    company = db.StringField(required=True)  # validation
    roles = db.ListField(default=["company_partner"], choices=ROLES)
    active = db.BooleanField(default=True)
