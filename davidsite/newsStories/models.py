import datetime

from django.db import models
from django.utils import timezone

class NewsArticle(models.Model):
    heading_text = models.CharField(max_length=50)
    pub_date_time = models.DateTimeField('date published')
    article_text = models.CharField(max_length=200)

    def __str__(self):
        return self.heading_text

    def was_published_recently(self):
        return self.pub_date_time >= timezone.now() - datetime.timedelta(days=1)

#    def __str__(self):
#        return self.article_text