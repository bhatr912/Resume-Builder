import os
import io
import base64
import tempfile
import subprocess

def compile_latex(latex_code, compiler='pdflatex', stop_on_first_error=True):
    """Compile LaTeX code to PDF"""
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            tex_file_path = os.path.join(tmpdir, 'document.tex')
            with open(tex_file_path, 'w') as tex_file:
                tex_file.write(latex_code)

            compile_command = [compiler, '-interaction=nonstopmode', '-output-directory', tmpdir, tex_file_path]
            if stop_on_first_error:
                compile_command.append('-halt-on-error')
            else:
                compile_command.append('-file-line-error')

            result = subprocess.run(compile_command, capture_output=True, text=True)

            pdf_file_path = os.path.join(tmpdir, 'document.pdf')
            if os.path.exists(pdf_file_path):
                with open(pdf_file_path, 'rb') as pdf_file:
                    pdf_content = pdf_file.read()
                pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')
                return pdf_base64, result.stdout + result.stderr, None
            else:
                return None, result.stdout + result.stderr, "PDF compilation failed"

    except Exception as e:
        return None, "", str(e)

def decode_pdf(pdf_base64):
    """Decode base64 PDF data to binary"""
    try:
        pdf_data = base64.b64decode(pdf_base64)
        return pdf_data, None
    except Exception as e:
        return None, str(e)
