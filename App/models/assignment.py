from datetime import date, datetime, timedelta

from App.database import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vieweeId =  db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    viewerId =  db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    feedId =  db.Column(db.Integer, db.ForeignKey('feed.id'))
    timeStamp = db.Column(db.DateTime(timezone=True), default=datetime.now())

    def __init__(self, vieweeId, viewerId):
        self.vieweeId = vieweeId
        self.viewerId = viewerId

    def toJSON(self):
        return{
            'id': self.id,
            'viewer-id': self.viewerId,
            'viewee-id': self.vieweeId,
            'feed-id': self.feedId,
            'timestamp': self.timeStamp,
        }