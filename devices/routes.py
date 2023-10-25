from flask import render_template, url_for, flash, redirect, request
from devices.forms import RegistrationForm, LoginForm
from devices import app, db, bcrypt
from devices.models import User_device, Device
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
# for static files
def home():
    return render_template('home.html', title="yasmin")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User_device(username=form.username.data,
                           email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User_device.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='=Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/devices')
@login_required
def device():
    column = request.args.get('column', 'DeviceID')  # Default sorting column
    order = request.args.get('order', 'asc')  # Default sorting order

    # Validate sorting parameters to prevent SQL injection
    allowed_columns = ['DeviceID', 'DeviceName',
                       'DeviceType', 'DeviceLocation']
    if column not in allowed_columns:
        column = 'DeviceID'
    if order not in ['asc', 'desc']:
        order = 'asc'

    # Modify the database query to include sorting
    if order == 'asc':
        devices = Device.query.order_by(getattr(Device, column))
    else:
        devices = Device.query.order_by(getattr(Device, column).desc())

    return render_template('device.html', title='Devices', devices=devices)
