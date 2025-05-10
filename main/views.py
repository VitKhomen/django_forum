from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q

from posts.models import Post


class BasePostListView(View):
    template_name = ''
    paginate_by = 6

    def get_queryset(self, request):
        return Post.objects.all().order_by('-created_at')

    def get_context_data(self, request, posts):
        paginator = Paginator(posts, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return {
            'posts': page_obj,
            'page_obj': page_obj,
            'paginator': paginator,
            'is_paginated': page_obj.has_other_pages(),
            'count': paginator.count
        }

    def get(self, request):
        posts = self.get_queryset(request)
        context = self.get_context_data(request, posts)
        return render(request, self.template_name, context)


class MainView(BasePostListView):
    template_name = 'main/start_page.html'


class SearchView(BasePostListView):
    template_name = 'main/search.html'
    paginate_by = 10

    def get_queryset(self, request):
        query = request.GET.get('q', '').strip()
        if not query:
            return Post.objects.none()
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct().order_by('-created_at')

    def get_context_data(self, request, posts):
        context = super().get_context_data(request, posts)
        context['query'] = request.GET.get('q', '')
        return context
