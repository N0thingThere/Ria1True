from django.contrib import admin
from .models import Movie, Review

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ["title", "description", "image", "price"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)