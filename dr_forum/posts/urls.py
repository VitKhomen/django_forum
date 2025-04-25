from django.urls import path

from .views import PostCreateView, PostDetailView, PostUpdateView, \
    PostDeleteView, UserPostListView


urlpatterns = [
    path('create-post/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('user/<str:username>/posts/',
         UserPostListView.as_view(), name='user_posts'),
]
