from App.models import *
from App.database import db

def create_feed():
    feed = Feed()
    db.session.add(feed)
    db.session.commit()
    return feed

def get_feed():
    return Feed.query.first() 

def append_assignment_to_feed(assignment):
    feed = get_feed()
    feed.assignments.append(assignment)
    db.session.commit()
    return True

def append_subscriber_to_feed(profile):
    feed = get_feed()
    feed.subscribers.append(profile)
    db.session.commit()
    return True
