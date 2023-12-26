from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(email='testuser@example.com', password='testpass')

        # Create some posts for testing
        self.post1 = Post.objects.create(title='Post 1', body='Content 1', author=self.user)
        self.post2 = Post.objects.create(title='Post 2', body='Content 2', author=self.user)

        # Create an API client for making requests
        self.client = APIClient()

    def test_list_posts(self):
        # Test listing all posts
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/v1/blogs/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_post(self):
        # Test creating a new post
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New Post', 'body': 'New Content','author':self.user.id}
        response = self.client.post('/api/v1/blogs/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 3)

    def test_retrieve_post(self):
    # Test retrieving a single post
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/v1/blogs/posts/{self.post1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Post 1')


    def test_update_post(self):
        # Test updating a post
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Post', 'body': 'Updated Content','author':self.user.id}
        response = self.client.put(f'/api/v1/blogs/posts/{self.post1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=self.post1.id).title, 'Updated Post')

    def test_delete_post(self):
        # Test deleting a post
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/v1/blogs/posts/{self.post1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)
