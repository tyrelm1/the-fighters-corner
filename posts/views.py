from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']  # Specify the fields to include in the form

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']  # Specify the fields to include in the form

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('post_list')  # Redirect to post list upon successful deletion

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Assuming you have authentication
            comment.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = CommentForm()
    return redirect('post_detail', pk=post_id)  # Redirect to post detail page if comment form is not valid
