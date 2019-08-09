from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, my_logout


urlpatterns = [
    path('', home, name="home"),
    path('login/', auth_views.LoginView, name='login'),
    path('logout/',auth_views.LoginView, name='logout'),
]


