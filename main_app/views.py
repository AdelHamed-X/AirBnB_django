from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import State, Amenity, Place, User, City, Review

def index(request):
    states = State.objects.all()
    amenities = Amenity.objects.all()
    places = Place.objects.all()
    context = {
        "states": states,
        "amenities": amenities,
        "places": places,
    }
    return render(request, 'index.html', context)


def advanced(request):
    states = State.objects.all()
    amenities = Amenity.objects.all()
    places = Place.objects.all()
    context = {
        "states": states,
        "amenities": amenities,
        "places": places,
    }
    return render(request, '4-hbnb.html', context)
