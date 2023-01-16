from django.urls import path
from .views import homePageView, resumePageView, aboutMePageView
        
urlpatterns = [
    path("", homePageView, name="home"),  
    ]     