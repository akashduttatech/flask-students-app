from app import db
from datetime import datetime
from app.models.class_models import ClassModel
from app.models.section_models import SectionModel
from app.models.stream_models import StreamModel

class StudentModel(db.Model):
    __tablename__ = "students"

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    # Foreign keys
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=True)
    stream_id = db.Column(db.Integer, db.ForeignKey('streams.id'), nullable=True)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    class_ = db.relationship(ClassModel, backref='students')
    section = db.relationship(SectionModel, backref='students')
    stream = db.relationship(StreamModel, backref='students')

    def __repr__(self):
        return (
            f'<StudentModel {self.name} - {self.class_.class_name} - {self.section.section_name} - {self.age}>'
        )
