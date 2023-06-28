from django.urls import path
from .views import anime, marvelDc, comic, otros, manga

urlpatterns = [
    path('anime/', anime , name='anime'),
    path('marvelDc/', marvelDc , name='marvelDc'),
    path('comic/', comic , name='comic'),
    path('manga/', manga , name='manga'),
    path('otros/', otros , name='otros'),
]
