from django.urls import path

from .views import (
    AllPostView, UsersPostView,
    PostDetailView, NotPublishedView,
    PostUpdateView, CreatePostsView,
    CreateCommentView, CommentListView, contact_us_view)

app_name = 'blog'
urlpatterns = [
    path('', AllPostView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/create_comment/', CreateCommentView.as_view(), name='create_comment'),
    path('create_post/', CreatePostsView.as_view(), name='create_post'),
    path('user_post/', UsersPostView.as_view(), name='post_user_list'),
    path('user_post/archive/', NotPublishedView.as_view(), name='archive'),
    path('user_post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/comments/', CommentListView.as_view(), name='post_comments'),
    path('contactus/', contact_us_view, name='contact_us'),
]
