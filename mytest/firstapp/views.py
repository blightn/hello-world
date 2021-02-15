from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import FirstApp

class FirstAppListView(ListView):
    """Просмотр записей"""

    model = FirstApp
    template_name = 'firstapp/list.html'
    context_object_name = 'point'


from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import FirstAppForm
from django.urls import reverse_lazy

class FirstAppCreateView(CreateView):
    """ создание """
    model = FirstApp
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/operations.html'
    form_class = FirstAppForm
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if form.is_valid():
            form.save()
        return super().form_valid(form)