from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.home,name="index"),
    path('projects',views.projects,name="projects"),
    path('contact',views.contact,name="contact"),
    path('resume',views.resume,name="resume"),
]
