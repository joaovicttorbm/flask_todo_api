from flask import Flask
from app.auth.auth_routes import auth
from app.routes.task_routes import routes
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth, url_prefix="/api/auth")
    app.register_blueprint(routes, url_prefix="/api")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

