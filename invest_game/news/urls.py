from django.urls import path
from . import views

urlpatterns = [
    """
    끝이 /news/ 로 끝날 때는 PostList가 처리
    """
    path('', views.PostList.as_view())
]
