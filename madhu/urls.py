from django.urls import path
from.import views

urlpatterns = [
     path("",views.base,name="base"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("service",views.service,name="service"),
    path("contact",views.contact,name="contact"),
    path("booking",views.booking,name="booking"),
    path("team",views.team,name="team"),
    path("menu",views.menu,name="menu"),
    path("testimonial",views.testimonial,name="testimonial")
    
    
    
    
]