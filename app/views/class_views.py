from flask import render_template
from flask_login import login_required
from app.models.class_models import ClassModel

def class_routes(app):
    """
    Register routes for class-related views.
    """
    @app.route('/classes/', methods=['GET'])
    @login_required
    def classes():
        classes = ClassModel.query.order_by(ClassModel.id.asc()).all()
        context = {
            'title': 'Classes',
            'classes': classes,
        }
        return render_template('public/classes/classes.html', **context)