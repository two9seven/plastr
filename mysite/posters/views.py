from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.utils import timezone

from posters.models import Poster

class PosterListView(ListView):

    model = Poster

    def get_context_data(self, **kwargs):
        context = super(PosterListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
