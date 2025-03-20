from django.urls import path 
from .views import HomeView , AboutView 
urlpatterns = [
    path('' ,HomeView , name="home page" )  , 
    path("home/" , HomeView , name="home url"),
    path("about/" , AboutView , name="about url"),

]