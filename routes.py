from flask import Flask
from api import api_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

# Create the app instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
