"""Create the URL patterns for learning_logs."""

from django.urls import path
from . import views


# Maps the home page, topics list, and individual topic pages to their view functions

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]