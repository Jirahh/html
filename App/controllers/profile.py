from App.models import *
from App.database import db

def create_profile():
    profile = Profile()
    db.session.add(profile)
    db.session.commit()
    return profile

def get_all_profiles():
    return Profile.query.all()

def get_all_profiles_json():
    profiles = Profile.query.all()
    if not profiles:
        return []
    profiles = [profile.toJSON() for profile in profiles]
    return profiles