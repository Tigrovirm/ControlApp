from django.urls import path
from .views import ListPost, DetailPost, CreatePost, EditPost, DeletePost, HomeView

app_name = "ControlApp"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create_post/", CreatePost.as_view(), name="create_post"),
    path("posts/", ListPost.as_view(), name="posts"),
    path("posts/<int:pk>/", DetailPost.as_view(), name="detail_post"),
    path("edit_post/<int:pk>/", EditPost.as_view(), name="edit_post"),
    path("posts/<int:pk>/delete/", DeletePost.as_view(), name="delete_post")
]