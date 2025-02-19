from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import get_object_or_404, render

# Create your models here.

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(default='No description available')
    image = models.ImageField(upload_to='movies/', default='movies/placeholder.png')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"
    
def movie_detail(request, movie_id):
     movie = get_object_or_404(Movie, movie_id=movie_id)
     reviews = Review.objects.filter(movie=movie)
     return render(request, "movielibrary/movie_detail.html", {'movie': movie, 'reviews': reviews})






# class Searchbar(models.Model):
 #   search_text = models.CharField(max_length=200)
 #   description = models.TextField()

 #   def __str__(self):
 #       return self.name