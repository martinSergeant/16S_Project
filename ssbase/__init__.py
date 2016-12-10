from flask import Flask


app = Flask(__name__)

def create_app():
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/') 
    return app
       