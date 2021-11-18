from sqlalchemy import Boolean, Column, ForeignKey, DateTime, \
    Integer, String, Text, Float

from app import db

class HouseSpecs(db.Model):
    """HouseSpecs"""
    __tablename__ = 'houses_specs'
    id = Column(Integer, primary_key=True)
    accommodates = Column(Integer)
    bathrooms = Column(Integer)
    cleaning_fee = Column(Boolean, default=False)
    review_scores_rating = Column(Integer)
    beds = Column(Integer)
    property_type = Column(String(100))
    room_type = Column(String(100))
    bed_type = Column(String(100))
    cancellation_policy = Column(String(100))
    city = Column(String(100))

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))