""" A moduls that has all the models for the database """
from typing import Any
from django.db import models
from uuid import uuid4
from datetime import datetime


class BaseModel(models.Model):
    """ A base model for all db models """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        """ String representation for each instance """
        if hasattr(self, "name"):
            return f"{self.name}"
        else: 
            return f"{self.__class__.__name__}: {self.id}"
    

class User(BaseModel):
    """ Main User class """
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)


class State(BaseModel):
    """ Main State class """
    name = models.CharField(max_length=255, null=False)


class City(BaseModel):
    """ Main City clas """
    name = models.CharField(max_length=255, null=False)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities", null=False)


class Amenity(BaseModel):
    """ Main Amenity class """
    name = models.CharField(max_length=255, null=False)


class Place(BaseModel):
    """ Main Place class """
    user_id = models.ManyToManyField(User, related_name="places", null=False)
    name = models.CharField(max_length=255, null=False)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name="places", null=False)
    description = models.CharField(max_length=255)
    number_rooms = models.IntegerField(default=0)
    number_bathrooms = models.IntegerField(default=0)
    max_guest = models.IntegerField(default=0)
    price_by_night = models.IntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Review(BaseModel):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="reviews", null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", null=False)
    text = models.CharField(max_length=255)
