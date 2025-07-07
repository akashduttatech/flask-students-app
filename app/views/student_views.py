from flask import render_template
from flask_login import login_required
from app.models.student_models import StudentModel


def student_routes(app):
    """
    Register routes for student-related views.
    """
    @app.route('/students/', methods=['GET'])
    @login_required
    def students():
        
        students = StudentModel.query.order_by(StudentModel.id.asc()).all()
        print(f"Students: {students}")
        context = {
            'title': 'Students',
            'students': students,
        }
        return render_template('public/students/students.html', **context)
