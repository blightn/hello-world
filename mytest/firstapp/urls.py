from django.urls import path
from .views import (
  FirstAppCreateView,
  FirstAppListView,
  FirstAppUpdateView,
  FirstAppDeleteView,
  FirstAppDetailView
  )


app_name = 'firstapp'

urlpatterns = [
    path('create/', FirstAppCreateView.as_view(), name='create'),
    path('list/', FirstAppListView.as_view(), name='list'),
    path('edit/<int:pk>', FirstAppUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', FirstAppDeleteView.as_view(), name='delete'),
    path('details/<int:pk>', FirstAppDetailView.as_view(), name='details'),
]