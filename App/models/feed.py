from datetime import date, datetime, timedelta

from App.database import db

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscribers = db.relationship('Profile', backref='feed')
    assignments = db.relationship('Assignment', backref='feed')
    last_refresh = db.Column(db.DateTime(timezone=True), default=datetime.now())

    def toJSON(self):
        return{
            'id': self.id,
            'last-refresh': self.last_refresh,
            'subscribers': [subscriber.toJSON() for subscriber in self.subscribers],
            'assignments': [assignment.toJSON() for assignment in self.assignments],
        }

    def refresh(self):
        current_time = datetime.now()
        time_since_last_refresh = current_time - self.last_refresh

        if time_since_last_refresh.days >= 1:
            self.last_refresh = current_time
            return True
        return False