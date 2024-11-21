from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL,echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
#define a simple orm model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable =False)
    age = Column(Integer, nullable=False)



Base.metadata.create_all(engine)
#create a new session
session = SessionLocal()
#create
#new_user= User(name='JosephAnnan',age=27)
#session.add(new_user)
#session.commit()

#session.close()


#read
users = session.query(User).all()
print("All users")
for user in users:
    print(user.id,user.name,user.age)


#session.close()


#update
user_to_update = session.query(User).filter_by(name='joseph').first()
if(user_to_update):
    user_to_update.age = 45
    session.commit()


#session.close()

#delete
user_to_delete = session.query(User).filter_by(name='joseph').first()
if(user_to_delete):
    session.delete(user_to_delete)
    session.commit()

#read
users = session.query(User).all()
print("All users")
for user in users:
    print(user.id,user.name,user.age)


session.close()
