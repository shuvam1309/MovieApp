import click
from flask.cli import with_appcontext
from package import db
from package.models import User, Movie


@click.command(name="recreate_table")
@with_appcontext
def dropnCreateDb():
    print("Dropping database...")
    db.drop_all()
    print("Database dropped...\nCreating new db...")
    db.create_all()
    print("New db created.")


@click.command(name="create_admin")
@with_appcontext
def createAdmin():
    mail = input("Enter user email: ")
    user = User.query.filter_by(email=mail).first()
    if user:
        user.admin = True
        db.session.add(user)
        db.session.commit()
        print("User permission elevated to master.")
    else:
        print("User not found")

@click.command(name="create_user")
@with_appcontext
def createUser():
    email = input("Enter user email: ")
    password = input("Enter user password: ")
    user = User(email=email, password=password, admin=False)
    db.session.add(user)
    db.session.commit()
    print("User added successfully.")


from package import app