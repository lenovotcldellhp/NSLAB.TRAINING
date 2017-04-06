from django.db import models

# Create your models here.
class NewsList(models.Model):
	num = models.IntegerField(primary_key = True)
	title = models.TextField()
	url = models.TextField()

class NewsInfo(models.Model):
	num = models.IntegerField()
	title = models.TextField()
	info = models.TextField()
