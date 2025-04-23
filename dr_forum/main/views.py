from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q

from posts.models import Post


class MainView(View):
    def get(self, request):
        query = request.GET.get('q', '')

        if query:
            posts = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by('-created_at')
        else:
            posts = Post.objects.all().order_by('-created_at')

        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'main/start_page.html', {
            'posts': page_obj,
            'query': query
        })
