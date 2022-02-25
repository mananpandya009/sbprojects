from models import User, db
from app import app


db.drop_all()
db.create_all()

#adding users in the table User
user1 = User(first_name='Black', last_name="Panther", image_url="https://tinyurl.com/2p855svz")
user2 = User(first_name='Iron', last_name="Man", image_url="https://tinyurl.com/599mujsv")
user3 = User(first_name='Thor', last_name="Odinson", image_url="https://tinyurl.com/3dfw832d")
  
#Add new objects to session, so they'll persist
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

#Commit--otherwise, this never gets saved
db.session.commit()