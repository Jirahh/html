from App.database import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    feedId = db.Column(db.Integer, db.ForeignKey('feed.id'))
    images = db.relationship('Image', backref='profile')
    ratingsRecieved = db.relationship('Rating', backref='target', foreign_keys='Rating.targetId')
    ratingsCreated = db.relationship('Rating', backref='creator', foreign_keys='Rating.creatorId')
    rankingsCreated = db.relationship('Ranking', backref='creator')
    averageRating = db.Column(db.Integer, default=0)
    viewerAssignments = db.relationship('Assignment', backref='viewer', foreign_keys='Assignment.viewerId')
    vieweeAssignments = db.relationship('Assignment', backref='viewee', foreign_keys='Assignment.vieweeId')

    def toJSON(self):
        return{
            'id': self.id,
            'feedId': self.feedId,
            'userId': self.userId,
            'images': [image.toJSON() for image in self.images],
            'ratings-received': [rating.toJSON() for rating in self.ratingsRecieved],
            'ratings-created': [rating.toJSON() for rating in self.ratingsCreated],
            'rankings-created': [ranking.toJSON() for ranking in self.rankingsCreated],
            'average-rating': self.averageRating,
            'viewer-assignments': [viewerAssignment.toJSON() for viewerAssignment in self.viewerAssignments],
            'viewee-assignments': [vieweeAssignment.toJSON() for vieweeAssignment in self.vieweeAssignments],
        }

        def get_average_rating(self):
            pass
