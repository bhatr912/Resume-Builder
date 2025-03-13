from flask import request, jsonify
from services.db_service import get_collection
from models.template import Template
from bson import ObjectId

def register_template_routes(app):
    @app.route('/get-templates', methods=['GET'])
    def get_templates():
        templates_collection = get_collection('Template')
        if templates_collection is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        templates = templates_collection.find({})
        templates_info = {}
        
        for template in templates:
            template_obj = Template.from_dict(template)
            template_id = str(template.get('_id'))
            templates_info[template_id] = {
                "id": template_id,
                "name": template_obj.name,
                "category": template_obj.category,
                "image_url": template_obj.image_url,
                "exampleprompt": template_obj.example_prompt
            }
            
        return jsonify(templates_info)
