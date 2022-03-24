from django.urls import path
from stats_maker import views

urlpatterns = [
    path('', views.stats_maker, name='stats_maker'),
]