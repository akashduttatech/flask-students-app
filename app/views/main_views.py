from flask import render_template


def main_routes(app):
    """
    Register main routes for the application.
    """
    
    @app.route('/')
    def home():
        return render_template('public/home.html')

    @app.route('/about')
    def about():
        return render_template('public/about.html')
