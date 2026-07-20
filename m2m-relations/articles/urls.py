from django.urls import path
from articles.views import ArticlesListView

urlpatterns = [
    path('', ArticlesListView.as_view(), name='articles'),
]
