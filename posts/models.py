from django.db import models
from django.conf import settings
from django.urls import reverse

from taggit.managers import TaggableManager

from utils.models import SlugifyMixin


class Post(SlugifyMixin, models.Model):
    title = models.CharField(max_length=200)
    url = models.SlugField(unique=True, blank=True, max_length=100)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/',
                              default='post_images/default.png')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.url})
