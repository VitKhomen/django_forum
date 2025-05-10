from django.urls import path

from .views import PostCreateView, PostDetailView, PostUpdateView, \
    PostDeleteView, UserPostListView, TaggedPostView


urlpatterns = [
    path('create-post/', PostCreateView.as_view(), name='create_post'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('user/<slug:slug>/posts/',
         UserPostListView.as_view(), name='user_posts'),
    path('tags/<slug:tag>/', TaggedPostView.as_view(), name='tagged_posts'),
]
