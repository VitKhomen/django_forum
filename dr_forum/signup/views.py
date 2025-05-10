from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from signup.forms import CustomUserCreationForm, UserLoginForm, EmailChangeForm
from signup.models import CustomUser
from posts.models import Post
from utils.models import SlugMixin


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


class ProfileView(LoginRequiredMixin, SlugMixin, DetailView):
    model = CustomUser
    template_name = 'signup/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter(
            author=self.object
        ).order_by('-created_at')
        return context


class PassChangeView(PasswordChangeView):
    template_name = 'signup/pass_change.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.request.user.url})


class EmailChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = EmailChangeForm
    template_name = 'signup/email_change.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.object.url})
