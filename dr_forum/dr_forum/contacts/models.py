from django.db import models


class Contacts(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=50)
    subject = models.CharField(verbose_name='Subject', max_length=100)
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.subject
