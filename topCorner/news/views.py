from django.views.generic.list import ListView
from stadia.models import Post
from django.views.generic import DetailView

# Create your views here.

class IndexView(ListView):
    model: Post
    template_name = "news/index.html"
    def get_queryset(self):
        return Post.objects.order_by('published_date')
class NewsDetail(DetailView):
    template_name = "news/item.html"
    model = Post