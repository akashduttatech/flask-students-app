from flask import render_template
from flask_login import login_required


def students_routes(app):
    """
    Register routes for student-related views.
    """
    @app.route('/students/', methods=['GET'])
    @login_required
    def students():
        students = [
            {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'status': 'Y'},
            {'name': 'Bob', 'age': 22, 'major': 'Mathematics', 'status': 'Y'},
            {'name': 'Charlie', 'age': 21, 'major': 'Physics', 'status': 'N'},
        ]
        context = {
            'title': 'Students',
            'students': students,
        }
        return render_template('public/students/students.html', **context)
