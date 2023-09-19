#!/usr/bin/env python3

from app import app
from models import db, Game, Review, User

if __name__ == 'main':
    with app.app_context():
        import ipdb; ipdb.set_trace()