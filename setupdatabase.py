from basic import db, User
# create all tables model --> table
db.create_all()

matt = User('mathennessey@gmail.com','matt', '08-14-1999')
john = User('john@gmail.com','john','07-09-1983')

db.session.add_all([matt,john])

db.session.commit()

# print(matt.email)