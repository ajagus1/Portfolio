from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, ma #imports db, an instance of SQLAlchemy that you defined in the config.py module. This gives models.py access to SQLAlchemy attributes and methods.

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    
class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True

class Person(db.Model):#defines the Person class. Inheriting from db.Model gives Person the SQLAlchemy features to connect to the database and access its tables.
    __tablename__ = "person" #connects the class definition to the person database table.
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), nullable=False)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = db.relationship(
        Note,
        backref="person",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Note.timestamp)"
    )
    
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        include_relationships = True
        
note_schema = NoteSchema()
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)