from django.urls import path
from .views import (
  FirstAppListView,
  FirstAppCreateView,
  FirstAppUpdateView
  )


app_name = 'firstapp'

urlpatterns = [
    path('list/', FirstAppListView.as_view(), name='list'),
    path('create/', FirstAppCreateView.as_view(), name='create'),
    path('edit/<int:pk>', FirstAppUpdateView.as_view(), name='edit'),
]