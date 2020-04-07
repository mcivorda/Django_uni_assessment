from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsArticle


def index(request):
    latest_articles_list = NewsArticle.objects.order_by('-pub_date')[:5]
    output = ', '.join([n.heading_text for n in latest_articles_list])
    return HttpResponse(output)

def detail(request, NewsArticle_id):
    return HttpResponse("You're looking at question %s." % NewsArticle_id)

def results(request, NewsArticle_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % NewsArticle_id)

def vote(request, NewsArticle_id):
    return HttpResponse("You're voting on question %s." % NewsArticle_id)