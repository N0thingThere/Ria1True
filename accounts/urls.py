from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.registration, name='accounts.registration'),
    path("login/", views.login, name="login"),
    path('orders/', views.orders, name='accounts.orders'),
    path('change_password',views.change_password, name='accounts.change_password'),
]