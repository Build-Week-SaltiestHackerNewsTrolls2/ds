from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

db = SQLAlchemy()

#migrate = Migrate()

class User(db.Model):
    User_id = db.Column(db.BigInteger, primary_key=True)
    Username = db.Column(db.String, nullable=False)
    Saltiness = db.Column(db.Integer)

class Comment(db.Model):
    Comment_id = db.Column(db.BigInteger, primary_key=True)
    Username = db.Column(db.String, nullable=False)
    Comment = db.Column(db.String, nullable=False)
    Saltiness = db.Column(db.Integer)

def parse_records(database_records):

    parse_records = []
    for record in database_records:
        print(record)
        parse_records =record.__dict__
        del parsed_record['_sa_instance_state']
        parse_records.append(parse_records)
    return parse_records
