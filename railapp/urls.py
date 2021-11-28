from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.Contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),
    path('confirmation/', views.Confirmation, name="confirmation"),
    path('faq/', views.faq, name="faq"),
]