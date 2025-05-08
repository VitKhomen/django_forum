from django import forms
from .models import Post
from taggit.forms import TagWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'content', 'image', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
