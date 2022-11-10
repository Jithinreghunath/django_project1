from django import views
from django.urls import path,include
# from .import views

from . import views

urlpatterns = [
    path('', views.index),
    path('myapp/',views.question_1),
     path('<int:id>/',views.option)
    
]