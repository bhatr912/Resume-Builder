from routes.user_routes import register_user_routes
from routes.template_routes import register_template_routes
from routes.latex_routes import register_latex_routes

def register_routes(app):
    """Register all routes with the Flask app"""
    register_user_routes(app)
    register_template_routes(app)
    register_latex_routes(app)
