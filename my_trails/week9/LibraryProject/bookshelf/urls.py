#nothing for now
from django.urls import path
from . import views

urlpatterns = [ path ('', views.landing, name = 'landing'),
               path ('room1/', views.room1, name = 'room1'),
               path ("room2/", views.room2, name = "room2" ), 
               
               ]