from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate


db = SQLAlchemy()

#migrate = Migrate()


class Salty_user(db.Model):
    index = db.Column(db.BigInteger, primary_key=True)
    User_ID = db.Column(db.BigInteger)
    Username = db.Column(db.String, nullable=False)
    Saltiness = db.Column(db.String)


class Salty_comment(db.Model):
    index = db.Column(db.BigInteger, primary_key=True)
    Comment_ID = db.Column(db.String)
    User_ID = db.Column(db.BigInteger)
    Username = db.Column(db.String)
    Comment = db.Column(db.String)
    Saltiness = db.Column(db.String)


def parse_records(database_records):

    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
