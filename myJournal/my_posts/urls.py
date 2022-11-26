from django.urls import path
from . import views
from .views import PostDayArchiveView


urlpatterns = [
    path('<int:year>/<str:month>/<int:day>/',
         PostDayArchiveView.as_view(),
         name="archive_day"),
]
