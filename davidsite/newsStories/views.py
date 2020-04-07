from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import NewsArticle


def index(request):
    latest_articles_list = NewsArticle.objects.order_by('-pub_date_time')[:5]
    #    template = loader.get_template('newsStories/index.html')
    context = {'latest_article_list': latest_articles_list}
    return render(request, 'newsStories/index.html', context)


def detail(request, NewsArtice_id):
    article = get_object_or_404(NewsArticle, pk=NewsArtice_id)
    return render(request, 'newsStories/index.html', {'NewsArticle': article})


def results(request, NewsArticle_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % NewsArticle_id)


def vote(request, NewsArticle_id):
    return HttpResponse("You're voting on question %s." % NewsArticle_id)
