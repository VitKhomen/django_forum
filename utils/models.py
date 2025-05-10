from django.db import models
from utils.slugify_utils import generate_unique_slug


class SlugifyMixin(models.Model):
    # из какого поля брать текст для slug
    slug_source_field = ['title', 'username',]
    slug_field_name = 'url'          # куда сохранять slug
    slug_max_length = 100            # максимальная длина slug

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        slug_field = getattr(self, self.slug_field_name)
        if not slug_field:
            field_value = ''
            for field_name in self.slug_source_field:
                field_value = getattr(self, field_name, '')
                if field_value:
                    break
            if field_value:
                slug = generate_unique_slug(
                    self,
                    field_value,
                    slug_field_name=self.slug_field_name,
                    max_length=self.slug_max_length
                )
                setattr(self, self.slug_field_name, slug)
        super().save(*args, **kwargs)


class SlugMixin:
    slug_field = 'url'
    slug_url_kwarg = 'slug'
