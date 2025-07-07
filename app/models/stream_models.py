from app import db

class StreamModel(db.Model):
    __tablename__ = 'streams'

    id = db.Column(db.Integer, primary_key=True)
    stream_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<StreamModel {self.stream_name}>'