from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publications/', views.PublicationListView.as_view(), name='publications'),
    path('presentations/', views.presentations, name='presentations'),
]