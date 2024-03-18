from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
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
    fields = ['title', 'content']

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('post_list')

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = None
    if request.method == 'POST':
        comment = post.comments.filter(author=request.user).first()
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)
    return redirect('post_detail', pk=pk)

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_edit.html', {'form': form})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    return render(request, 'comment_delete.html', {'comment': comment})
