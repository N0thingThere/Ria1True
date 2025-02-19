from django.urls import path
from . import views
urlpatterns = [
    path("", views.landing, name="landing"),
    path("registration/", views.registration, name="registration"),
    path("logout/", views.logout, name="logout"),
    path("landing/", views.home, name="home"),
    path("account/", views.account, name="account"),
    path("movie/", views.movie, name="movie"),
    path("moviespage/", views.moviespage, name="moviespage"),
#    path("cart/", views.cart, name="cart"),
#    path("add_to_cart/<int:movie_id>/", views.add_to_cart, name="add_to_cart"),
#    path("remove_from_cart/<int:cart_item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("movie_detail/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("movie/<int:movie_id>/add_review/", views.create_review, name='movies.create_review'),
    path('<int:movie_id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:movie_id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
]