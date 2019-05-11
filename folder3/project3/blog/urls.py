from django.urls import path
from . import views
#. represent current directory, to import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]