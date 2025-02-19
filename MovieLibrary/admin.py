from django.contrib import admin
from .models import Movie, User

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ["title","rating"]


admin.site.register(Movie, MovieAdmin)
