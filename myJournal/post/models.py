from django.db import models
from django.db.models import CharField, DateField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = CharField(max_length=250, default='title')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
