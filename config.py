import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGODB_URI = os.getenv('MONGODB_URI')
DB_NAME = "Latex"

# Google AI Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
AI_MODEL = "gemini-1.5-flash"

# Flask Configuration
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
PORT = int(os.environ.get('PORT', 5000))
HOST = '0.0.0.0'

# LaTeX Compilation
DEFAULT_COMPILER = 'pdflatex'
