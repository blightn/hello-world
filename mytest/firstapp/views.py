from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import FirstApp

class FirstAppListView(ListView):
    """Просмотр записей"""

    model = FirstApp
    template_name = 'firstapp/list.html'
    context_object_name = 'point'