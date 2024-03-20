from django.contrib import admin  # Import admin module

from django.urls import path, include
from posts.views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, add_comment,
    comment_edit, comment_delete
)
from accounts.views import signup_view 
from events.views import event_list, event_detail  # Import views from the events app

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("admin/", admin.site.urls),  
    path("summernote/", include("django_summernote.urls")),
    path("", PostListView.as_view(), name="home"),
    path("posts/", include("posts.urls")),
    path("accounts/", include("allauth.urls")),  
    path('events/', include('events.urls')),  
]
