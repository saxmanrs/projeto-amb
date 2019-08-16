from django.urls import path
from .views import cbo_new


urlpatterns = [

path('cbo/', cbo_new, name="cbo_new"),

]