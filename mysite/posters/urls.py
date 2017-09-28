from django.conf.urls import url
from . import views
from posters.views import PosterListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', PosterListView.as_view(), name='index'),
] 
