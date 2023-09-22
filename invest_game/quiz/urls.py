from django.urls import path
from . import views

urlpatterns = [
    path('', views.Quiz_list),
]



