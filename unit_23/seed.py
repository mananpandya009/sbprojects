from models import User, db, Post
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

user1 = User(first_name='Black', last_name="Panther", image_url="https://tinyurl.com/2p855svz")
user2 = User(first_name='Iron', last_name="Man", image_url="https://tinyurl.com/599mujsv")
user3 = User(first_name='Thor', last_name="Odinson", image_url="https://tinyurl.com/3dfw832d")

post1 = Post(title="Post 1", content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", created_at = "2022-02-26 18:58:54", user_id = 1)
db.session.add(post1)
db.session.commit()