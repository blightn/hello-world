from django.shortcuts import render

from django.views.generic import ListView
from .models import FirstApp

from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import FirstAppForm
from django.urls import reverse_lazy

# Create your views here.

class FirstAppListView(ListView):
    """ Просмотр записей """

    model = FirstApp
    template_name = 'firstapp/list.html'
    context_object_name = 'context'

class FirstAppCreateView(CreateView):
    """ Создание записи """
    model = FirstApp
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/operations.html'
    form_class = FirstAppForm
    #fields = '__all__'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_context_data(self):
        context = super().get_context_data()
        context['action'] = 'Добавить запись'
        return context

class FirstAppUpdateView(UpdateView):
    """ Изменение записи """
    model = FirstApp
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/operations.html'
    form_class = FirstAppForm
    #fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['action'] = 'Изменить запись'
        return context