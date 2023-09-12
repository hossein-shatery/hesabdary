from django.urls import path
from . import views

urlpatterns = [
    path('kharj/', views.defkharj, name='defkharj'),
    path('dakhl/', views.defdakhl, name='defdakhl'),
]
