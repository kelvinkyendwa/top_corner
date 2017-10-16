from django.views.generic.list import ListView
from stadia.models import Post

# Create your views here.

class IndexView(ListView):
    model: Post
    template_name = "news/index.html"
    def get_queryset(self):
        return Post.objects.order_by('published_date')
