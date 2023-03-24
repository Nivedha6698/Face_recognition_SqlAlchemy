from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:password@localhost/face_recognition')
Session = sessionmaker(bind=engine)
session = Session()

class Face(Base):
    __tablename__ = 'faces'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    features = Column(Text)

Base.metadata.create_all(engine)

session.close()
