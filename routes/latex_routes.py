from flask import request, jsonify, send_file
from services.db_service import get_collection
from services.ai_service import generate_latex_from_template, update_latex
from services.latex_service import compile_latex, decode_pdf
from models.template import Template
from bson import ObjectId
import io

def register_latex_routes(app):
    @app.route('/generate-latex', methods=['POST'])
    def generate_latex():
        templates_collection = get_collection('Template')
        if templates_collection is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        data = request.json
        prompt = data.get("prompt", "")
        template_id = data.get("template_id")
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        try:
            template_doc = templates_collection.find_one({"_id": ObjectId(template_id)})
            
            if not template_doc:
                return jsonify({"error": "Template not found"}), 404
            
            template = Template.from_dict(template_doc)
            latex_code, error = generate_latex_from_template(template, prompt)
            
            if error:
                return jsonify({"error": error}), 500
                
            return jsonify({"latex_code": latex_code}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/update-latex', methods=['POST'])
    def update_latex_route():
        data = request.json
        latex_code = data.get("latex_code", "")
        update_prompt = data.get("update_prompt", "")
        
        if not latex_code or not update_prompt:
            return jsonify({"error": "Both LaTeX code and update prompt are required"}), 400

        try:
            updated_latex, error = update_latex(latex_code, update_prompt)
            
            if error:
                return jsonify({"error": error}), 500
                
            return jsonify({"latex_code": updated_latex}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/compile-latex', methods=['POST'])
    def compile_latex_route():
        data = request.json
        latex_code = data.get("latex_code", "")
        options = data.get("options", {})
        
        if not latex_code:
            return jsonify({"error": "LaTeX code is required"}), 400

        try:
            compiler = options.get('compiler', 'pdflatex')
            stop_on_first_error = options.get('stopOnFirstError', True)
            
            pdf_base64, compile_output, error = compile_latex(
                latex_code, 
                compiler=compiler, 
                stop_on_first_error=stop_on_first_error
            )
            
            if error:
                return jsonify({
                    "error": error,
                    "compile_output": compile_output
                }), 500
                
            return jsonify({
                "pdf_base64": pdf_base64,
                "compile_output": compile_output
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/download-pdf', methods=['POST'])
    def download_pdf():
        data = request.json
        pdf_base64 = data.get("pdf_base64", "")
        
        if not pdf_base64:
            return jsonify({"error": "PDF content is required"}), 400

        try:
            pdf_data, error = decode_pdf(pdf_base64)
            
            if error:
                return jsonify({"error": error}), 500
                
            return send_file(
                io.BytesIO(pdf_data),
                mimetype='application/pdf',
                as_attachment=True,
                download_name='document.pdf'
            )

        except Exception as e:
            return jsonify({"error": str(e)}), 500
