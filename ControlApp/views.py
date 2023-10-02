from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = "ControlApp/home_page.html"

class ListPost(ListView):
    queryset = posts = Post.objects.all()
    context_object_name = "posts"
    template_name = "ControlApp/posts.html"

class DetailPost(DetailView):
    model = Post
    template_name = "ControlApp/detail_post.html"
    context_object_name = "post"

class CreatePost(CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "ControlApp/create_post.html"
    success_url = reverse_lazy("ControlApp:posts")

class EditPost(UpdateView):
    model = Post
    template_name = "ControlApp/edit_post.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("ControlApp:posts")

class DeletePost(DeleteView):
    model = Post
    template_name = "staffonly/delete_post.html"
    context_object_name = "post"
    success_url = reverse_lazy("ControlApp:posts")