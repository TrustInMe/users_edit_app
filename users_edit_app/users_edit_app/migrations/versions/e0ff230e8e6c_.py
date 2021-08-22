"""empty message

Revision ID: e0ff230e8e6c
Revises: 7715a520f681
Create Date: 2021-08-21 20:24:13.341994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0ff230e8e6c'
down_revision = '7715a520f681'
branch_labels = None
depends_on = None

from users_edit_app import User,Permission, db
from users_edit_app.utils import make_password_hash

def upgrade():
    permission_arr = [
        "edit users",
        "add users",
        "delete users"
    ]

    user = User(
        username="Admin",
        password=make_password_hash("default_password")
    )

    for permission in permission_arr:
        permission_obj = Permission(permission)
        db.session.add(permission_obj)
        user.permissions.append(permission_obj)
    db.session.add(user)
    db.session.commit()


def downgrade():
    pass
