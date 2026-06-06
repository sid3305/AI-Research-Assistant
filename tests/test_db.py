from app import create_app
from app.extensions import db

from app.models.user import User


app = create_app()

with app.app_context():

    user = User(
        username="siddhi",
        email="siddhi@example.com"
    )

    db.session.add(user)

    db.session.commit()

    print("User inserted successfully.")