from django.utils.text import slugify
from unidecode import unidecode


def generate_unique_slug(instance, field_value, slug_field_name='url', max_length=100):
    base_slug = slugify(unidecode(field_value))[:max_length]
    base_slug = base_slug.rstrip('-')
    slug = base_slug
    counter = 1
    ModelClass = instance.__class__

    while ModelClass.objects.filter(**{slug_field_name: slug}).exclude(pk=instance.pk).exists():
        suffix = f"-{counter}"
        available_length = max_length - len(suffix)
        slug = f"{base_slug[:available_length]}{suffix}"
        counter += 1

    return slug
