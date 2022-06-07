# Register your models here.
from django.contrib import admin
from .models import Rental
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list = "___all___"

    admin.site.register(Rental)