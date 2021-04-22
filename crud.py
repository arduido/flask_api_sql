from basic import db, User

#### create
user_2 = User('radical@gmail.com', 'Bryce', '09-14-1988')
db.session.add(user_2)
db.session.commit()

all_users = User.query.all()
print(all_users)


#### read
user_matt = User.query.filter_by(name='matt').first()
#this should print the repr of matt
print(user_matt)

#### update
user_bryce = User.query.filter_by(name='Bryce').first()
user_bryce.email = 'therealdeal@gmail.com'
db.session.add(user_bryce)
db.session.commit()
print(user_bryce)

#### delete
user_john = User.query.filter_by(name='john').first()
db.session.delete(user_john)
db.session.commit()

#### show all users
print(all_users)