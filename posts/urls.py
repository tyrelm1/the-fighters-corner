# urls.py

from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, add_comment,
    comment_edit, comment_delete
)
from accounts.views import signup_view 

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
     path('comment/<int:pk>/edit/', comment_edit, name='edit_comment'),  
    path('comment/<int:pk>/delete/', comment_delete, name='delete_comment'),
    path('signup/', signup_view, name='signup'),  
]
