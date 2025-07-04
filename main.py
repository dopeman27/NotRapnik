from flask import Flask
from config import Config
from extensions import db, migrate, login
from routes import bp as main_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
