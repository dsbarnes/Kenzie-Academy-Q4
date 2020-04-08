from django.urls import path
from . import views

urlpatterns = [
    path('<slug:twitter_user>/', views.profile, name='profile'),
    path('follow/<slug:twitter_user>/', views.follow, name='follow'),
    path('unfollow/<slug:twitter_user>/', views.unfollow, name='unfollow')
]