from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator
from django.views.generic.dates import DayArchiveView


class PostDayArchiveView(DayArchiveView):

    date_field = 'post_date'
    month_format = '%m'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)
