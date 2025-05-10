from django.urls import path
from comments.views import CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('post/<slug:slug>/comment/',
         CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/',
         CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment_delete'),
]
