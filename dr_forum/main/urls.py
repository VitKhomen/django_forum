from django.urls import path

from main import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('search/', views.SearchView.as_view(), name='search'),
]
