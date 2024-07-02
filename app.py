import flask
from models import *
from sqlalchemy import select
from flask_cors import CORS

app = flask.Flask(__name__)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://djangouser:djangopassword@localhost:5432/flaskdb"
# initialize the app with the extension
db.init_app(app)



@app.route("/")
def home():
    return "Hello, world"



@app.route("/users")
def list_users():
    import pdb; pdb.set_trace()
    users_select_query = db.select(User).order_by(User.firstname)
    users = db.session.execute(users_select_query).scalars()
    ret = []
    for user in users:
      details = {"id" : user.id,
         "firstname" : user.firstname,
         "lastname" : user.lastname,
         "email" : user.email,
         "phone" : user.ph_no
         }
      ret.append(details)
    return flask.jsonify(ret)




if __name__ == "__main__":
  init_db()
  app.run(port=5000)
