from django.urls import path
from . import views
from .views import PostDayArchiveView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('<int:year>/<str:month>/<int:day>/',
         login_required(PostDayArchiveView.as_view(), login_url='login'),
         name="archive_day"),
]
