from django.shortcuts import render
from rest_framework import generics 
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

