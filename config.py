import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DATABASE = os.path.join(BASE_DIR, 'instance', 'portfolio.db')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt', 'rtf', 'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp'}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB max upload size
    GITHUB_API_BASE = 'https://api.github.com'
