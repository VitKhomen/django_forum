from django.urls import path

from contacts import views

urlpatterns = [
    path('contacts/', views.ContactsCreateView.as_view(), name='contacts'),
    path('contacts/<slug:slug>/', views.ContactsDetailView.as_view(),
         name='contacts_answer'),
    path('contacts/<slug:slug>/update', views.ContactsUpdateView.as_view(),
         name='contacts_update'),
    path('contacts/<slug:slug>/delete', views.ContactsDeleteView.as_view(),
         name='contacts_delete'),
]
