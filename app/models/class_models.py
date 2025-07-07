from app import db

class ClassModel(db.Model):
    
    __tablename__ = 'classes'
    
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<ClassModel {self.class_name}>'