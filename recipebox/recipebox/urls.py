"""recipebox URL Configuration

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
from django.urls import path
# from recipebox.models import Author, Recipe
from .views import (
    index_view,
    recipes_view,
    author_view,
    add_recipe_view,
    edit_recipe_view,
    add_favorite_view,
    favorites_view,
    add_author_view,
    register_view,
    login_view,
    logut_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="home"),
    path('register/', register_view),
    path('login/', login_view),
    path('add_recipe/', add_recipe_view),
    path('edit_recipe/<int:id>/', edit_recipe_view, name="edit"),
    path('add_author/', add_author_view),
    path('recipes/<int:id>', recipes_view),
    path('add_favorite/<int:id>/', add_favorite_view, name='add_favorite'),
    path('favorites/<int:id>/', favorites_view, name='favorites'),
    path('author/<int:id>', author_view, name='author'),
    path('logout/', logut_view)
]
