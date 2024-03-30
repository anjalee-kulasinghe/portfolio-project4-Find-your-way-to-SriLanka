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


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.commenter.username} on {self.article.title}'
