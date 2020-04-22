from django.contrib import admin
from django.urls import path, include
from site_users import views
from django.conf.urls import handler404, handler500

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('buy/<str:company>/', views.buy, name='buy'),
    path('sell/<str:company>/', views.sell, name='sell'),
    path('finalize/<str:ticker>/<int:amount>/', views.finish_buy, name='finalize'),
    path('finalizesell/<str:ticker>/<int:amount>/', views.finish_sell, name='finalsell'),
    path('favorite/<str:company>/', views.add_to_following, name='favorite'),
    path('', include('site_users.urls'), name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name='logout')

]
