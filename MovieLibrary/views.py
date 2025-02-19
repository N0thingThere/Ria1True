from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Movie, Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
# from .forms import ReviewForm

def landing(request):
    return render(request, "movielibrary/landing.html")

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "movielibrary/registration.html", {'form': form})
'''
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'MovieLibrary/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'MovieLibrary/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('')
'''
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("moviespage")
    else:
        form = AuthenticationForm()
    return render(request, "movielibrary/login.html", {'form': form})

def logout(request):
    auth_logout(request)
    return redirect("landing")

def home(request):
    return render(request, "movielibrary/landing.html")

@login_required
def account(request):
    user = request.user
    return render(request, "movielibrary/account.html", {'user': user})

def movie(request):
    return render(request, "movielibrary/movie.html")

def moviespage(request):
    movies = Movie.objects.all()
    return render(request, "movielibrary/moviespage.html", {'movies': movies})

'''
@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.movie.price * item.quantity for item in cart_items)
    return render(request, "movielibrary/cart.html", {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, movie=movie)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart")

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect("cart")
'''
def movie_detail(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    template_data = {}
    template_data['title'] = movie.title
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(request, "movielibrary/movie_detail.html", {'template_data': template_data})
    #reviews = Review.objects.filter(movie=movie)
    #return render(request, "movielibrary/movie_detail.html", {'movie': movie, 'reviews': reviews})
'''
@login_required
def add_review(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    if request.method == 'POST' and request.POST['comment'] != '':
            review = Review()
            review.comment = request.POST['comment']
            review.user = request.user
            review.save()
            return redirect("movie_detail", movie_id=movie.id)
    else:
        return redirect("movie_detail", movie_id=movie.id)
'''
@login_required
def create_review(request, movie_id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(movie_id=movie_id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movie_detail', movie_id=movie_id)
    else:
        return redirect('movie_detail', movie_id=movie_id)
@login_required
def edit_review(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movie_detail', movie_id=movie_id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'MovieLibrary/edit_review.html',
            {'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movie_detail', movie_id=movie_id)
    else:
        return redirect('movie_detail', movie_id=movie_id)
@login_required
def delete_review(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id,
        user=request.user)
    review.delete()
    return redirect('movie_detail', movie_id=movie_id)
