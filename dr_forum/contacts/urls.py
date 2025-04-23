from django.urls import path

from contacts import views

urlpatterns = [
    path('contacts/', views.ContactsCreateView.as_view(), name='contacts'),
    path('contacts/<int:pk>/', views.ContactsDetailView.as_view(),
         name='contacts_answer'),
    path('contacts/<int:pk>/update', views.ContactsUpdateView.as_view(),
         name='contacts_update'),
    path('contacts/<int:pk>/delete', views.ContactsDeleteView.as_view(),
         name='contacts_delete'),
]
