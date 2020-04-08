from django.urls import path
from . import views

urlpatterns = [
    path('', views.write_tweet, name='write_tweet'),
    path('<int:id>/', views.single_tweet, name='single_tweet')
]