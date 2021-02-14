from django.urls import path
from .views import (
  FirstAppListView,
  )


app_name = 'firstapp'

urlpatterns = [
    path('list/', FirstAppListView.as_view(), name='list'),

]