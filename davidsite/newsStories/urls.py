from django.urls import path

from . import views

urlpatterns = [
    # ex: /news/
    path('', views.index, name='index'),
    # ex: /news/5/
    path('<int:NewsArticle_id>/', views.detail, name='detail'),
]