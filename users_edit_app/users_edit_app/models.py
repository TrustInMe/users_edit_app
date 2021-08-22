from flask_login import UserMixin
from flask import redirect, url_for

from users_edit_app import db, login_manager

permissions = db.Table(
    'permissions',
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Permission(db.Model):
    """
    Модель доступов.
    """

    __tablename__ = "permission"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self) -> str:
        return self.title

class User(db.Model, UserMixin):
    """
    Модель пользователей.

    Имеет связь many-to-many с доступами.
    """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    permissions = db.relationship(
        'Permission', 
        secondary=permissions, 
        lazy='subquery',
        backref=db.backref('permission', lazy=True)
    )
    

    def __init__(self, username, password, first_name=None, last_name=None):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


    def change_user_data(self, form_data):
        """
        Метод, предназначенный для изменения данных
        уже существующего пользователя.
        """
        self.username = form_data['username']
        self.first_name = form_data['first_name']
        self.last_name = form_data['last_name']

        for permission in form_data.getlist('permissions'):
            permission_obj = Permission.query.get(int(permission))
            self.permissions.append(permission_obj)

        db.session.add(self)
        db.session.commit()

        return redirect(url_for('users_list_page'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)