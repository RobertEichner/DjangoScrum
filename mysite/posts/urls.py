# posts/urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import HomePageView, CreatePostView

urlpatterns = [
    path("posts/", HomePageView.as_view(), name="posts"),
    path("postsUpload/", login_required(CreatePostView.as_view()), name="postsUpload"),
    path('<int:id>/', views.singlepost, name='singlepost'),
]
