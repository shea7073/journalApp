from django.db import models
from django.db.models import CharField
from ckeditor.fields import RichTextField



class Post(models.Model):
    title = CharField(max_length=250, default='title')
    body = RichTextField(blank=True, null=True)
