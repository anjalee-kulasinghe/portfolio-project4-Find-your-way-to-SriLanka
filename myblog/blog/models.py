from django.db import models
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=255)  # Title of the article
	content = HTMLField()  # Content of the article, allowing HTML formatting
	date = models.DateField(auto_now_add=True)  # Date when the article was created
	author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the article
	featured = models.BooleanField(default=False)  # Indicates if the article is featured
	likes = models.ManyToManyField(User, related_name='likes', blank=True)  # Users who liked the article