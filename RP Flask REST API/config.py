import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve() #creates the variable basedir pointing to the directory that the program is running in.
connex_app = connexion.App(__name__, specification_dir=basedir) #uses the basedir variable to create the Connexion app instance and give it the path to the directory that contains your specification file.


app = connex_app.app #creates a variable, app, which is the Flask instance initialized by Connexion.
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}" # tell SQLAlchemy to use SQLite as the database and a file named people.db in the current directory as the database file.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #turns the SQLAlchemy event system off.

db = SQLAlchemy(app) #initializes SQLAlchemy by passing the app configuration information to SQLAlchemy and assigning the result to a db variable.
ma = Marshmallow(app) 
