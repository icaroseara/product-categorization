import os
import dotenv

project_dir = os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)

ENV = os.getenv('ENV', 'development')
FEATURES = os.getenv('FEATURES', '').split(',')
MODELS_DIR = os.getenv('MODELS_DIR')
MODEL_FILE = os.getenv('MODEL_FILE')
