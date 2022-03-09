from models import PostTag, User, db, Post, Tag
from app import app


db.drop_all()
db.create_all()


#adding users in the table User
user1 = User(first_name='Black', last_name="Panther", image_url="https://tinyurl.com/2p855svz")
user2 = User(first_name='Iron', last_name="Man", image_url="https://tinyurl.com/599mujsv")
user3 = User(first_name='Thor', last_name="Odinson", image_url="https://tinyurl.com/3dfw832d")
  
#Add new objects to session, so they'll persist
db.session.add_all([user1,user2,user3])
#Commit--otherwise, this never gets saved
db.session.commit()

post1 = Post(title="Post 1", content="Lorem Ipsum", created_at = "2022-02-26 18:58:54", user_id = 1)
db.session.add(post1)
db.session.commit()

tag1 = Tag(name='Fun', tag_post=[PostTag(post_id=post1.id)])
tag2 = Tag(name='Even More')
tag3 = Tag(name='Bloop',tag_post=[PostTag(post_id=post1.id)])


db.session.add_all([tag1,tag2,tag3])
db.session.commit()

