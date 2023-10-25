from datetime import datetime
from devices import db
from devices import login_manager
from flask_login import UserMixin

# Flask-Login can manage user sessions. Start by adding the UserMixin to your User model. The UserMixin will add Flask-Login attributes to the model so that Flask-Login will be able to work with it.


@login_manager.user_loader
def load_user(user_id):
    return User_device.query.get(int(user_id))


class User_device(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}',' {self.image_file}')"


class Device(db.Model, UserMixin):
    DeviceID = db.Column(db.Integer, nullable=False, primary_key=True)
    DeviceName = db.Column(db.String(255), nullable=False)
    DeviceType = db.Column(db.String(255), nullable=False)
    DeviceLocation = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User('{self.DeviceID}', '{self.DeviceName}',' {self.DeviceType}', '{self.DeviceLocation})"
