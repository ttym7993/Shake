# -*- coding: utf-8 -*-
"""
    manage.py
    ----------------------------------------------
    Admin scripts

"""
from shake import manager

from app.app import app


@manager.command
def run(host='0.0.0.0', port=None, **kwargs):
    """[-host HOST] [-port PORT]
    Runs the application on the local development server.
    """
    app.run(host, port, **kwargs)


@manager.command
def run_wsgi():
    """Run the application using the WSGI protocol."""
    application = app


@manager.command
def syncdb():
    from app.models import db
    
    db.create_all()


@manager.command
def create_user(email, passw, **data):
    """[-login] LOGIN [-passw] PASSWORD
    Creates a new user.
    """
    from app.app import auth
    
    auth.create_user(login, passw, **data)


@manager.command
def change_password(login, passw):
    """[-login] LOGIN [-passw] NEW_PASSWORD
    Changes the password of an existing user."""
    from app.app import auth
    
    auth.change_password(login, passw)


@manager.command
def add_perms(login, *perms):
    """[-login] LOGIN [-perms] *PERMISSIONS
    Add permissions to the user
    """
    from app.models import db, User
    
    user = User.query.filter_by(login=login).first()
    if not user:
        raise ValueError(login)
    user.add_perms(perms)
    db.session.commit()


if __name__ == "__main__":
    manager.run(default='run')