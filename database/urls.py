from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publications/', views.PublicationListView.as_view(), name='publications'),
    path('presentations/', views.PresentationListView.as_view(), name='presentations'),
    path('travel/', views.TravelListView.as_view(), name='travel'),
    path('fellowships-and-grants/', views.GrantListView.as_view(), name='grants'),
    path('societies/', views.SocietyListView.as_view(), name='societies'),
]