from django.shortcuts import render
from rest_framework import generics 
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    