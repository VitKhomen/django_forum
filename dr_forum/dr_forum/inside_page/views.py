from urllib import request
from django.shortcuts import render
from django.views import View


class InsidePageView(View):
    def get(self, request):
        return render(request, 'inside_page/article.html')

# Create your views here.
