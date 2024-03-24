from app import views
from django.urls import path

urlpatterns = [
     path('',views.index,name="index"),
     path('about',views.about,name="about"),
     path('resume',views.resume,name="resume"),
     path('portfolio',views.portfolio,name="portfolio"),
     path('services',views.services,name="services"),
     path('contact',views.contact,name="contact"),
     path('savemessge',views.save,name="save")
]