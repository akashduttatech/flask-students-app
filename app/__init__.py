from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the SQLAlchemy object
db = SQLAlchemy()

# Initialize the LoginManager object
login_manager = LoginManager()
# Set the login_view for the login manager
login_manager.login_view = 'signin'
# Customize the message
login_manager.login_message = "You need to be logged in to view this page."
login_manager.login_message_category = "danger"

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    # Initialize the database with the app
    db.init_app(app)
    
    # Initialize the login manager with the app
    login_manager.init_app(app)
    
    # Import all models before create_all()
    from app.models.auth_models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        """
        Callback function to load a user by their ID.
        """
        return User.query.get(int(user_id))
    
    # Create database tables for all models for local development and testing purposes
    # with app.app_context():
    #     db.create_all()  # Create database tables
    #     print("Database tables created successfully.")
    
    # Register views
    from app.views.main_views import main_routes
    from app.views.auth_views import auth_routes
    from app.views.students_views import students_routes
    main_routes(app)
    auth_routes(app)
    students_routes(app)

    return app