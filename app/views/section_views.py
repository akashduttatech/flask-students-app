from flask import render_template
from flask_login import login_required
from app.models.section_models import SectionModel

def section_routes(app):
    """
    Register routes for section-related views.
    """
    @app.route('/sections/', methods=['GET'])
    @login_required
    def sections():
        sections = SectionModel.query.order_by(SectionModel.section_name.asc()).all()
        context = {
            'title': 'Sections',
            'sections': sections,
        }
        return render_template('public/sections/sections.html', **context)