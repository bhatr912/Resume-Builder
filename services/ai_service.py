import google.generativeai as genai
from config import GOOGLE_API_KEY, AI_MODEL

# Configure the Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)

def generate_latex_from_template(template, prompt):
    """Generate LaTeX code from a template using AI"""
    try:
        model = genai.GenerativeModel(AI_MODEL)
        
        template_latex = template.latex_code
        system_instruction = template.system_instruction
        
        full_prompt = f"{system_instruction}\n\nLaTeX Template:\n{template_latex}\n\nGenerate content using the provided template and guidelines with the following details:\n{prompt}"
        
        response = model.generate_content(full_prompt)
        return response.text.strip(), None
    except Exception as e:
        return None, str(e)

def update_latex(latex_code, update_prompt):
    """Update existing LaTeX code based on a prompt"""
    try:
        model = genai.GenerativeModel(AI_MODEL)
        
        # Craft a specific prompt for updating existing LaTeX code
        system_prompt = """You are a LaTeX expert. You will be provided with existing LaTeX code and a request to modify it. 
        Make only the requested changes while preserving the overall structure and formatting.
        Return only the modified LaTeX code without any explanations or markdown formatting."""
        
        full_prompt = f"{system_prompt}\n\nExisting LaTeX Code:\n{latex_code}\n\nRequested Changes:\n{update_prompt}\n\nModified LaTeX Code:"
        
        response = model.generate_content(full_prompt)
        return response.text.strip(), None
    except Exception as e:
        return None, str(e)
