from django.urls import path
from .views import (
  FirstAppListView,
  )
from .views import (
  FirstAppCreateView,
  )


app_name = 'firstapp'

urlpatterns = [
    path('list/', FirstAppListView.as_view(), name='list'),
    path('create/', FirstAppCreateView.as_view(), name='create'),

]