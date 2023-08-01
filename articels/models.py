from django.db import models

# Create your models here.
class Articels(models.Model):
    article_title=models.CharField(max_length=255)
    article_content=models.TextField()
