from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Note
from .forms import FirstAppForm


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'

class FirstAppCreateView(CustomLoginRequiredMixin, CreateView):
    # Создание записки

    model = Note
    template_name = 'firstapp/operations.html'
    #form_class = FirstAppForm  # get_context_data() got an unexpected keyword argument 'form'
    #fields = '__all__'         # get_context_data() got an unexpected keyword argument 'form'
    fields = ('title', 'text')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed. It should return an HttpResponse.
        form.instance.author = self.request.user
        if form.is_valid():
            form.save()
        return redirect('firstapp:list')
    
    def get_context_data(self):
        context = super().get_context_data()
        context['action'] = 'Добавить записку'
        return context

class FirstAppListView(CustomLoginRequiredMixin, ListView):
    # Просмотр записок

    model = Note
    template_name = 'firstapp/list.html'
    context_object_name = 'context'
    paginate_by = 15

    def get_queryset(self):
        self.object = Note.objects.filter(author=self.request.user)
        return self.object

class FirstAppDetailView(CustomLoginRequiredMixin, DetailView):
    # Просмотр деталей записки

    model = Note
    template_name = 'firstapp/details.html'
    context_object_name = 'context'
    form_class = FirstAppForm
    #fields = '__all__'

class FirstAppUpdateView(CustomLoginRequiredMixin, UpdateView):
    # Изменение записки

    model = Note
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/operations.html'
    #form_class = FirstAppForm  # get_context_data() got an unexpected keyword argument 'form'
    #fields = '__all__'         # get_context_data() got an unexpected keyword argument 'form'
    fields = ('title', 'text')

    def get_context_data(self):
        context = super().get_context_data()
        context['action'] = 'Изменить записку'
        return context

class FirstAppDeleteView(CustomLoginRequiredMixin, DeleteView):
    # Удаление записки

    model = Note
    success_url = reverse_lazy('firstapp:list')
    template_name = 'firstapp/delete.html'
    context_object_name = 'context'
    form_class = FirstAppForm
    #fields = '__all__'