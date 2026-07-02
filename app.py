from flask import Flask
from config import Config
import os

from routes.home import home_bp
from routes.upload import upload_bp
from routes.chat import chat_bp
from routes.summary import summary_bp
from database.db import db
from routes.chat import chat_bp
from routes.summary import summary_bp
from routes.dashboard import dashboard_bp   



def create_app():

    app = Flask(__name__)
    app.secret_key = "papermind_ai_secret"

    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(home_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(dashboard_bp)
    
    

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5002,
        debug=True,
        use_reloader=False
    )