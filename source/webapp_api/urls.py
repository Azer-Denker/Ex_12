from django.urls import path

from webapp_api.views import index_view

app_name = 'webapp_api'

urlpatterns = [
    path('', index_view, name='index')
]
