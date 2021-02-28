from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import FirstAppForm


class FirstAppCreateView(LoginRequiredMixin, CreateView):
    # Создание записки

    login_url = '/login/'

    model = Note
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/operations.html'
    form_class = FirstAppForm
    #fields = '__all__'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed. It should return an HttpResponse.
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def get_context_data(self):
        context = super().get_context_data()
        context['action'] = 'Добавить записку'
        return context

class FirstAppListView(LoginRequiredMixin, ListView):
    # Просмотр записок

    login_url = '/login/'

    model = Note
    template_name = 'firstapp/list.html'
    context_object_name = 'context'
    paginate_by = 15

    def get_queryset(self):
        self.object = Note.objects.filter(author=self.request.user)
        return self.object

class FirstAppDetailView(LoginRequiredMixin, DetailView):
    # Просмотр деталей записки

    login_url = '/login/'

    model = Note
    template_name = 'firstapp/details.html'
    context_object_name = 'context'
    form_class = FirstAppForm
    #fields = '__all__'

    def get_queryset(self):
        self.object = Note.objects.filter(author=self.request.user)
        return self.object

class FirstAppUpdateView(LoginRequiredMixin, UpdateView):
    # Изменение записки

    login_url = '/login/'

    model = Note
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/operations.html'
    form_class = FirstAppForm
    #fields = '__all__'

    def get_context_data(self):
        context = super().get_context_data()
        context['action'] = 'Изменить записку'
        return context

    def get_queryset(self):
        self.object = Note.objects.filter(author=self.request.user)
        return self.object

class FirstAppDeleteView(LoginRequiredMixin, DeleteView):
    # Удаление записки

    login_url = '/login/'

    model = Note
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/delete.html'
    context_object_name = 'context'
    form_class = FirstAppForm
    #fields = '__all__'