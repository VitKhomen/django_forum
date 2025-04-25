from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, \
    UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.http import Http404

from .models import Post
from .forms import PostForm


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class UserPostListView(ListView):
    User = get_user_model()
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 6

    def get_queryset(self):
        username = self.kwargs.get('username')
        try:
            user = self.User.objects.get(username=username)
        except self.User.DoesNotExist:
            raise Http404("Пользователь не найден")
        return Post.objects.filter(author=user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Посты пользователя {self.kwargs.get('username')}"
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    context_object_name = 'post'
    fields = ['title', 'content', 'image']

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise Http404("У вас нет прав на редактирование этого поста.")
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('main')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise Http404("У вас нет прав на удаления этого поста.")
        return super().dispatch(request, *args, **kwargs)


def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Сортировка по дате
    return render(request, 'main/index.html', {'posts': posts})
