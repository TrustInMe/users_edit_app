from users_edit_app import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user

from users_edit_app.utils import check_password, make_password_hash
from users_edit_app.models import User, Permission, permissions


@app.route("/", methods=['GET', 'POST'])
def login_page():
    error_msg = None
    if request.method == "POST":
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('users_list_page'))
        else:
            error_msg = "Wrong username or password. Please try again"

    return render_template(
        "pages/login_page.html",
        title="Login page",
        form_error=error_msg,
    )


@app.route("/users", methods=['GET', 'POST'])
@login_required
def users_list_page():
    if request.method == "POST":
        deleting_user = User.query.get(int(request.json['id']))
        db.session.delete(deleting_user)
        db.session.commit()
    users = User.query.all()
    add_permission = Permission.query.filter_by(title="add users").first()
    edit_permission = Permission.query.filter_by(title="edit users").first()
    delete_permission = Permission.query.filter_by(title="delete users").first()

    return render_template(
        "pages/users_list.html",
        users=users,
        add_permission=add_permission,
        edit_permission=edit_permission,
        delete_permission=delete_permission,
    )



@app.route("/users/add_user", methods=['GET', 'POST'])
@login_required
def add_user():
    error_msg = None
    permissions = Permission.query.all()
    if request.method == "POST":
        if request.form['username'] and request.form['password'] and request.form.getlist('permissions'):
            if not bool(User.query.filter_by(username=request.form['username']).first()):
                user = User(
                    username=request.form['username'],
                    password=make_password_hash(request.form['password']),
                    last_name=request.form['last_name'],
                    first_name=request.form['first_name'],
                )
                for permission in request.form.getlist('permissions'):
                    permission_obj = Permission.query.get(int(permission))
                    user.permissions.append(permission_obj)

                db.session.add(user)
                db.session.commit()
                return redirect(url_for('users_list_page'))
            else:
                error_msg = "Username already taken"
        else:
            error_msg = "Username, password and permissions are required"

    return render_template(
        "pages/add_user.html",
        permissions=permissions,
        form_error=error_msg,
    )

@app.route("/users/<id>", methods=['GET', 'POST'])
@login_required
def edit_user(id):
    error_msg = None
    permissions = Permission.query.all()
    user = User.query.get(id)

    if request.method == "POST":
        if request.form['username'] and request.form.getlist('permissions'):
            if user.username == request.form['username']:
                user.change_user_data(request.form)
            else: 
                if not bool(User.query.filter_by(username=request.form['username']).first()):
                    user.change_user_data(request.form)
                else:
                    error_msg = "Username already taken"
        else:
            error_msg = "Username and permissions are required"

    return render_template(
        "pages/edit_user.html",
        permissions=permissions,
        user=user,
        form_error=error_msg,
    )

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))