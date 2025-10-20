from recipes.views import home, contato, sobre
from django.urls import path



urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]