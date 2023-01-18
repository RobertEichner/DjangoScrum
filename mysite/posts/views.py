from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, Http404
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PostForm
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "posts/posts.html"


@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "posts/postsUpload.html"
    success_url = reverse_lazy("posts")


def singlepost(request, id):
    try:
        image_file = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return FileResponse(open(image_file.cover.path, 'rb'))

