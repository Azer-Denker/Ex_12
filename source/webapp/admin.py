from django.contrib import admin
from webapp.models import Advert, Category


class AdvertAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)


admin.site.register(Advert)
admin.site.register(Category)
