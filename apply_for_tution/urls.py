
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.ApplicationListView.as_view(), name='application-list'),
    path('create/', views.ApplicationCreateView.as_view(), name='application-create'),
]
