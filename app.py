import os
from flask import Flask
from config import Config
from models.db import init_db, close_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.dirname(app.config['DATABASE']), exist_ok=True)

    app.teardown_appcontext(close_db)
    init_db(app)  # safe to call every start; uses CREATE TABLE IF NOT EXISTS

    from routes.auth import auth_bp
    from routes.dashboard import dashboard_bp
    from routes.resume import resume_bp
    from routes.github import github_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(github_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
