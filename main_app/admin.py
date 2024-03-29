from django.contrib import admin
from main_app.models import State, City, Amenity, Place, User

admin.site.register(City)
admin.site.register(State)
admin.site.register(Amenity)
admin.site.register(Place)
admin.site.register(User)

# Register your models here.
