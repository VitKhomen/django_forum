from django.urls import path

from .views import InsidePageView

urlpatterns = [
    path('article/', InsidePageView.as_view(), name='article')
]
