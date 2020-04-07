from django.shortcuts import get_object_or_404, render
from .models import NewsArticle


def index(request):
    latest_articles_list = NewsArticle.objects.order_by('-pub_date_time')[:5]
    context = {'latest_article_list': latest_articles_list}
    return render(request, 'newsStories/index.html', context)


def detail(request, newsarticle_id):
    article = get_object_or_404(NewsArticle, pk=newsarticle_id)
    return render(request, 'newsStories/index.html', {'NewsArticle': article})
