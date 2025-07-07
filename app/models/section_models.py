from app import db

class SectionModel(db.Model):
    
    __tablename__ = 'sections'
    
    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<SectionModel {self.section_name}>'