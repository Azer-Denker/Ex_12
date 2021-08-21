from django.urls import path, include

from api_v2.views import AdvertView, AdvertDetailView


app_name = 'api_v2'


advert_urls = [
    path('', AdvertView.as_view(), name='adverts'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='detail'),

]


urlpatterns = [
    path('adverts/', include(advert_urls)),
]
