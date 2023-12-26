from django.urls import path
from posts import views
from . import views
urlpatterns = [
    path('create_user/',views.CreateUserView.as_view(),name='create'),
    path('token/',views.CreateUserTokenView.as_view(),name='create_token'),
    path('me/',views.ManageUserView.as_view(),name='manage_user')
]
