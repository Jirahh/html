from App.models import *
from App.database import db

def create_assignment(vieweeId, viewerId):
    assignment = Assignment(vieweeId, viewerId)
    db.session.add(assignment)
    db.session.commit()
    return assignment
