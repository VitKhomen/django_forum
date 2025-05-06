from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, \
    UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponseRedirect

from .models import Post, Comment
from .forms import PostForm, CommentForm
from utils.models import SlugMixin


@method_decorator(login_required, name='dispatch')
class PostCreateView(SlugMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.url})


class UserPostListView(ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        username = self.kwargs.get('slug')
        User = get_user_model()
        try:
            user = User.objects.get(url=username)
        except User.DoesNotExist:
            raise Http404("Пользователь не найден")
        return Post.objects.filter(author=user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs.get('slug')
        context['title'] = f"Посты пользователя {self.kwargs.get('slug')}"
        return context


class PostDetailView(View):
    template_name = 'posts/post_detail.html'

    def get_context(self, request, slug):
        post = get_object_or_404(Post, url=slug)
        context = {
            'post': post,
            'popular_tags': Post.tags.most_common()[:10],
            'last_posts': Post.objects.all().order_by('-id')[:3],
            'comment_form': CommentForm()
        }
        return context

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context(request, slug)
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        context = self.get_context(request, slug)
        context['comment_form'] = comment_form

        if comment_form.is_valid():
            Comment.objects.create(
                post=context['post'],
                author=request.user,
                text=comment_form.cleaned_data['text']
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        return render(request, self.template_name, context)


class TaggedPostView(ListView):
    template_name = 'posts/tagged_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context


class PostUpdateView(SlugMixin, UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    context_object_name = 'post'
    fields = ['h1', 'title', 'description', 'content', 'image', 'tags']

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.url})

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            raise Http404("У вас нет прав на редактирование этого поста.")
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(SlugMixin, DeleteView):
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
