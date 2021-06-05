from application import db
from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    Enum
)

class Movie(db.Model):
    __tablename__ = 'Movie'
    movie_id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(50))
    movie_format = Column(Enum('VHS', 'DVD', 'Streaming'))
    length = Column(Integer)
    release_date = Column(Integer)
    rating = Column(Integer)

    def __repr__(self):
        return '<Movie {}>'.format(self.title)
