from django.urls import path
from .views import task_1_view

app_name = 'api_v1'

urlpatterns = [
    path('add/', task_1_view, name='add'),
    path('subtract/', task_1_view, name='subtract'),
    path('multiply/', task_1_view, name='multiply'),
    path('divide/', task_1_view, name='divide'),
]