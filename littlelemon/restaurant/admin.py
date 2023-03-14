from django.contrib import admin

# Register your models here.
# to register the model in admin.py

from .models import Menu
from .models import Booking


admin.site.register(Menu)
admin.site.register(Booking)
