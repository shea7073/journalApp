from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator
from django.views.generic.dates import DayArchiveView


# Create your views here.
class PostDayArchiveView(DayArchiveView):

    date_field = 'post_date'
    month_format = '%m'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     obj= Post.objects.filter(owner=self.request.user).latest('post_date')
    #     field_object = Post._meta.get_field('post_date')
    #     field_value = field_object.value_from_object(obj)
    #     year = field_value.year
    #     day = field_value.day
    #     month = field_value.month
    #     context["day"] = day
    #     context['month'] = month
    #     context['year'] = year
    #     return context

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)
