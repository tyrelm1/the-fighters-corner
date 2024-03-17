from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView,add_comment )
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', PostCreateView.as_view(template_name='signup.html'), name='signup'),
]
