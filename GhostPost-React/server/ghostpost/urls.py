"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .models import Post
from . import views

admin.site.register(Post)

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add_post'),
    path('downvote/<int:pk>', views.down_vote),
    path('upvote/<int:pk>', views.up_vote),
    path('boasts/', views.boasts_only, name='boasts'),
    path('roasts/', views.roasts_only, name='roasts'),
    path('most_recent', views.most_recent, name='most_recent'),
    path('up_votes_ascending', views.up_votes_ascending,
         name='votes_ascending'),
    path('up_votes_descending', views.up_votes_descending,
         name='votes_descending'),
    path('down_votes_ascending', views.down_votes_ascending,
         name='down_votes_descending'),
    path('down_votes_descending', views.down_votes_descending,
         name='down_votes_descending'),
    path('api/', include(router.urls))
]
