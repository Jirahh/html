from datetime import date, datetime, timedelta

from App.database import db

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creatorId =  db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    targetId = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    timeStamp = db.Column(db.DateTime(timezone=True), default=datetime.now())
    
    def __init__(self, creatorId, targetId, value):
        self.creatorId = creatorId
        self.targetId = targetId
        self.value = value
    
    def toJSON(self):
        return{
            'id': self.id,
            'creatorId': self.creatorId,
            'targetId': self.targetId,
            'value': self.value,
            'time-stamp': self.timeStamp
        }
