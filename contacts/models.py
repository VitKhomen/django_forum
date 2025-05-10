from django.db import models

from utils.models import SlugifyMixin


class Contacts(SlugifyMixin, models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=100)
    title = models.CharField(verbose_name='Title', max_length=200)
    message = models.TextField(verbose_name='Message')
    url = models.SlugField(unique=True, blank=True, max_length=100)

    def __str__(self):
        return self.title
