from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import re
from . import db
from .models import Registration



views = Blueprint('views', __name__)
email_regex = r'^\S+@\S+\.\S+$'
mobile_regex = r'^\d{10}$'

@views.route('/')
def home():
    users = Registration.query.all()
    return render_template('home.html', users=users)

@views.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        email = request.form['email'].strip()
        dob = request.form['dob']
        gender = request.form['gender']
        mobile = request.form['mobile'].strip()

        if len(first_name) < 2 or len(last_name)<2:
            flash("Name must be at least 2 characters long.", "error")
            return render_template('add.html')

        if not re.match(email_regex, email):
            flash("Invalid email address.", "error")
            return render_template('add.html')

        if Registration.query.filter_by(email=email).first():
            flash("Email already exists.", "error")
            return render_template('add.html')

        if not dob:
            flash("Date of Birth is required.", "error")
            return render_template('add.html')

        if not gender:
            flash("Gender is required.", "error")
            return render_template('add.html')

        if not re.match(mobile_regex, mobile):
            flash("Mobile number must be 10 digits.", "error")
            return render_template('add.html')

        user = Registration( first_name = first_name,  last_name = last_name, email=email, dob=dob, gender=gender, mobile=mobile)
        db.session.add(user)
        db.session.commit()
        flash("User added successfully!", "success")
        return redirect(url_for('views.home'))

    return render_template('add.html')

@views.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = Registration.query.get_or_404(id)
    if request.method == 'POST':
        first_name = request.form['first_name'].strip()
        last_name = request.form['last_name'].strip()
        email = request.form['email'].strip()
        dob = request.form['dob']
        gender = request.form['gender']
        mobile = request.form['mobile'].strip()

        if len(first_name) < 2 or len(last_name)<2:
            flash("Name must be at least 2 characters long.", "error")
            return render_template('add.html')

        if not re.match(email_regex, email):
            flash("Invalid email address.", "error")
            return render_template('edit.html', user=user)

        if user.email != email and Registration.query.filter_by(email=email).first():
            flash("Email already exists.", "error")
            return render_template('edit.html', user=user)

        if not dob:
            flash("Date of Birth is required.", "error")
            return render_template('edit.html', user=user)

        if not gender:
            flash("Gender is required.", "error")
            return render_template('edit.html', user=user)

        if not re.match(mobile_regex, mobile):
            flash("Mobile number must be 10 digits.", "error")
            return render_template('edit.html', user=user)

        user. first_name =  first_name
        user. last_name =  last_name
        user.email = email
        user.dob = dob
        user.gender = gender
        user.mobile = mobile
        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for('views.home'))

    return render_template('edit.html', user=user)

@views.route('/delete/<int:id>')
def delete(id):
    user = Registration.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted.", "success")
    return redirect(url_for('views.home'))