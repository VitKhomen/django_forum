from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from comments.models import Comment
from comments.forms import CommentForm

from posts.models import Post


class CommentCreateView(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                author=request.user,
                text=form.cleaned_data['text'],
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )

        return redirect(post.get_absolute_url())


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_update.html'

    def get_success_url(self):
        return self.object.content_object.get_absolute_url()

    def test_func(self):
        return self.request.user == self.get_object().author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_delete.html'

    def get_success_url(self):
        return self.object.content_object.get_absolute_url()

    def test_func(self):
        return self.request.user == self.get_object().author
