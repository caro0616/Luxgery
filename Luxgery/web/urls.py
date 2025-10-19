from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),  # ✅ Nueva ruta
    path("testimonios/", views.testimonios, name="testimonios"),
    path("contacto/", views.contacto, name="contacto"),
]
