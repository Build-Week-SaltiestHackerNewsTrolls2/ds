from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate


db = SQLAlchemy()

#migrate = Migrate()


class salty_user(db.Model):
    User_id = db.Column(db.BigInteger, primary_key=True)
    Username = db.Column(db.String, nullable=False)
    Saltiness = db.Column(db.Integer)


class salty_comment(db.Model):
    index = db.Column(db.BigInteger, primary_key=True)
    Comment_ID = db.Column(db.String)
    User_ID = db.Column(db.BigInteger)
    Username = db.Column(db.String)
    Comment = db.Column(db.String)
    Saltiness = db.Column(db.String)


def parse_records(database_records):

    parse_records = []
    for record in database_records:
        print(record)
        parse_records = record.__dict__
        del parsed_record['_sa_instance_state']
        parse_records.append(parse_records)
    return parse_records
