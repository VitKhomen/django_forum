from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .forms import CustomUserCreationForm, UserLoginForm
from .models import CustomUser
from posts.models import Post


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup/register.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class LoginView(LoginView):
    template_name = 'signup/login.html'
    authentication_form = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('main')


class LogoutView(LogoutView):
    next_page = reverse_lazy('main')


@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    user_posts = Post.objects.filter(
        author=user_profile).order_by('-created_at')
    return render(request, 'signup/profile.html', {'user_profile': user_profile, 'user_posts': user_posts})
