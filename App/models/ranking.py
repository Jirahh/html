from datetime import date, datetime, timedelta

from App.database import db

class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creatorId =  db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    imageId =  db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    timeStamp = db.Column(db.DateTime(timezone=True), default=datetime.now())
    
    
    def __init__(self, creatorId, imageId, value):
        self.creatorId = creatorId
        self.imageId = imageId
        self.value = value
    
    def toJSON(self):
        return{
            'id': self.id,
            'creatorId': self.creatorId,
            'imageId': self.imageId,
            'value': self.value,
            'time-stamp': self.timeStamp
        }
