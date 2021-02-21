from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FirstAppForm
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from .models import FirstApp

# Create your views here.

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

class FirstAppListView(ListView):
    """ Просмотр записей """

    model = FirstApp
    template_name = 'firstapp/list.html'
    context_object_name = 'context'
    paginate_by = 15

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

class FirstAppDeleteView(DeleteView):
    """ Удаление записи """
    model = FirstApp
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/delete.html'
    context_object_name = 'context'
    form_class = FirstAppForm
    #fields = '__all__'

class FirstAppDetailView(DetailView):
    """ Просмотр деталей записи """
    model = FirstApp
    template_name = 'firstapp/details.html'
    context_object_name = 'context'
    form_class = FirstAppForm
    #fields = '__all__'