from django.views.generic import ListView
from .models import Article


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles/news.html'
    context_object_name = 'object_list'
    ordering = '-published_at'
