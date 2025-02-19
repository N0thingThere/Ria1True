from django.contrib import admin
from .models import Movie, User

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ["title", "description", "image", "price"]


admin.site.register(Movie, MovieAdmin)
