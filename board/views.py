from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy



class PostListView(ListView):
    model = Post
    template_name = 'board/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name= "board/post_detail.html"
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'board/post_create.html'
    fields = ['title', 'content']
    success_url = '/board/posts'

class PostUpdateView(UpdateView):
    model = Post
    template_name="board/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy('board:post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name= "board/post_delete.html"
    success_url= "/board/posts"

