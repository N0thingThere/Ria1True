from django.shortcuts import render
from .models import Movie
# Create your views here.


def index(request):
    template_data = {}
    template_data['title'] = 'movies'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html', {'templaste_data': template_data})