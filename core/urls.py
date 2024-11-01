from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('contacts/', views.contacts, name='contacts'),
    path('predications/', views.predications, name='predications'),
    path('agenda/', views.agenda, name='agenda'),
]
