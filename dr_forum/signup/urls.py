from django.urls import path

from signup.views import RegisterView, LoginView, LogoutView, \
    ProfileView, EmailChangeView, PassChangeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
    path('email/change/', EmailChangeView.as_view(), name='email_change'),
    path('password/change/', PassChangeView.as_view(), name='pass_change'),

]
