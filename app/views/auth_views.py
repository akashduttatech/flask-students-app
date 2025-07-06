from flask import render_template, redirect, flash, session, url_for
from app.forms.auth_forms import SignupForm, SigninForm
from app import db
from app.models.auth_models import User
from flask_login import login_user, logout_user, current_user



def auth_routes(app):
    @app.route('/signin', methods=['GET', 'POST'])
    def signin():
        form = SigninForm()
        
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            
            if user and user.check_password(password):
                # store the user in session
                login_user(user)
                return redirect(url_for('students'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
            
            return redirect('signin')

        return render_template('public/auth/signin.html', title='Sign In', form=form)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        form = SignupForm()

        if form.validate_on_submit():
            fullname = form.fullname.data
            email = form.email.data
            password = form.password.data
            
            # Create a new user instance
            new_user = User(fullname=fullname, email=email)
            new_user.set_password(password)

            try:
                # Add the new user to the database
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                flash(f"An error occurred while creating your account: {str(e)}", 'danger')
            else:
                return redirect('signin')

        return render_template('public/auth/signup.html', title='Sign Up', form=form)

    @app.route('/signout', methods=['GET'])
    def signout():
        logout_user()
        return redirect(url_for('signin'))

