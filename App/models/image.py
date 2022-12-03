from App.database import db

#Images uploaded by users
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profileId =  db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    rankings = db.relationship('Ranking', backref='ranking')
    overallRank =  db.Column(db.Integer)

    def __init__(self, profileId):
        self.profileId = profileId
        self.rank = -1

    def toJSON(self):
        return{
            'id': self.id,
            'userId': self.profileId,
            'overall-rank': self.overallRank,
            'rankings': [ranking.toJSON() for ranking in self.rankings]
        }
