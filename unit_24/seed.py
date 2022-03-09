from sqlalchemy import false
from models import Pet, db
from app import app


db.drop_all()
db.create_all()

#adding users in the table User
pet1 = Pet(name='panther', species="terrier", photo_url="https://tinyurl.com/nhc2emyt", age=2, notes="very funny dog with great expressions", available=True)
pet2 = Pet(name='ironhound', species="retriever", photo_url="https://images.wsj.net/im-221140?width=1280&size=1", age=3, notes="very cute dog with great speed",available=True)
pet3 = Pet(name='thor', species="poodle", photo_url="https://tinyurl.com/mvyptyju",age=1, notes="very fiesty dog with great anger",available=False)
  
#Add new objects to session, so they'll persist
db.session.add_all([pet1,pet2,pet3])
#Commit--otherwise, this never gets saved
db.session.commit()
