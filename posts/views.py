from django.shortcuts import render
from rest_framework import generics 
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

