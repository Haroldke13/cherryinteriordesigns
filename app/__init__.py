from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate() 

def create_database():
    db.create_all()
    print('Database Created')

def create_app():
    # Initialize the flask app
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'do_not_show_this_to_anyone_100'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
    
    # Configure upload folders:
    # Profile pictures remain in static/profile_pics
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/profile_pics')
    # Product images will be stored in the media folder at the project root
    app.config['PRODUCT_FOLDER'] = os.path.join(app.root_path, 'media')

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    # Login logic
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    @login_manager.user_loader
    def load_user(id):
        from .models import Customer  # import here to avoid circular import
        return Customer.query.get(int(id))
    
    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        create_database()

    return app