from app.errors.handlers import errors
from flask import Flask


app = Flask(__name__)

# Flask konfigurieren
app.config['SECRET_KEY'] = '71100e0e1a235b6e67a441043f514d52'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(errors)

from app import routes
