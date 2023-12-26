from django.urls import path
from .views import PostListView, PostDetailView
urlpatterns = [
path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
path("posts/", PostListView.as_view(), name="post_list"),
]