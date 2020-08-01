from django.urls import path
from .import views

urlpatterns=[
path('', views.home, name='home'),
path('sentiment/', views.sentiment_view, name='sentiment'),
path('summarize/', views.summarize_view, name='summarize'),
path('visualize/', views.visualizer_view, name='visualize')


]
