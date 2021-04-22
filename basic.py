import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
api = Api(app)
# ======================setting up the db ===================


class User(db.Model):

    __tablename__= 'users'

    email = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(80))
    dob = db.Column(db.Text)

    def __init__(self, email, name, dob):
        self.email = email
        self.name = name
        self.dob = dob

    def json(self):
        return f"{self.name} your username is: {self.email}"

    class UserNames(Resource):

        def get(self, name):

            person = User.query.filter_by(name=name).first()

            if person:
                return person.json()

            return {'name':None}, 404

        def delete(self, name):

            person = User.query.filter_by(name=name).first()
            db.session.delete(person)
            db.session.commit()
    
    class CreateUser(Resource):

        def post(self, name, email, dob):

            person = User(name=name, email=email, dob=dob)
            db.session.add(person)
            db.session.commit()
            
            return person.json()

    class AllUsers(Resource):
        def get(self):
            people = User.query.all()

            return [peep.json() for peep in people]
    
    api.add_resource(UserNames, '/name/<string:name>')
    api.add_resource(CreateUser, '/create/<string:name>/<string:email>/<string:dob>')
    api.add_resource(AllUsers, '/users')

if __name__ == '__main__':
    app.run(debug=True)