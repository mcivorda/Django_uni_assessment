from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import NewsArticle


def index(request):
    latest_articles_list = NewsArticle.objects.order_by('-pub_date_time')[:5]
    template = loader.get_template('newsStories/index.html')
    context = {
        'latest_article_list': latest_articles_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, NewsArticle_id):
    return HttpResponse("You're looking at question %s." % NewsArticle_id)


def results(request, NewsArticle_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % NewsArticle_id)


def vote(request, NewsArticle_id):
    return HttpResponse("You're voting on question %s." % NewsArticle_id)
