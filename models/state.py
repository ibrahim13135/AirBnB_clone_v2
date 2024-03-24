#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete-orphan',
                          backref="state", passive_deletes=True)

    @property
    def cities(self):
        """Getter method to return the list of City objects linked to the current State"""
        city_list = []
        if models.storage.__class__.__name__ != "DBStorage":
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
        return city_list
