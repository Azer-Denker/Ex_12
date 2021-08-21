from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, \
    UserPassesTestMixin
from django.core.paginator import Paginator
from rest_framework import status
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Advert
from webapp.forms import AdvertForm, BROWSER_DATETIME_FORMAT
from .base_views import SearchView


class IndexView(SearchView):
    template_name = 'advert/index.html'
    context_object_name = 'adverts'
    paginate_by = 2
    paginate_orphans = 0
    model = Advert
    ordering = ['-created_at']
    search_fields = ['title__icontains', 'author__icontains']

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset.filter(is_delete=False))
        data = queryset.filter(is_delete=False)
        return data


class AdvertMassActionView(PermissionRequiredMixin, View):
    redirect_url = 'webapp:index'
    permission_required = 'webapp.delete_advert'
    queryset = None

    def has_permission(self):
        if super().has_permission():
            return True
        adverts = self.get_queryset()
        author_ids = adverts.values('author_id')
        for item in author_ids:
            if item['author_id'] != self.request.user.pk:
                return False
        return True

    def post(self, request, *args, **kwargs):
        if 'delete' in self.request.POST:
            return self.delete(request, *args, **kwargs)
        return redirect(self.redirect_url)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return redirect(self.redirect_url)

    def get_queryset(self):
        if self.queryset is None:
            ids = self.request.POST.getlist('selected_adverts', [])
            self.queryset = self.get_queryset().filter(id__in=ids)
        return self.queryset


class AdvertView(DetailView):
    template_name = 'advert/advert_view.html'
    model = Advert
    if model.status is ['new', 'rejected']:
        queryset = status.HTTP_400_BAD_REQUEST


class AdvertCreateView(LoginRequiredMixin, CreateView):
    template_name = 'advert/advert_create.html'
    form_class = AdvertForm
    model = Advert

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.author = self.request.user
        advert.save()
        form.save_m2m()
        return redirect('webapp:advert_view', pk=advert.pk)


class AdvertUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'advert/advert_update.html'
    form_class = AdvertForm
    model = Advert
    permission_required = 'webapp.change_advert'

    def has_permission(self):
        advert = self.get_object()
        return super().has_permission() or advert.author == self.request.user

    def get_initial(self):
        return {'publish_at': make_naive(self.object.publish_at).strftime(BROWSER_DATETIME_FORMAT)}

    def form_valid(self, form):
        advert = form.save()
        return redirect('webapp:advert_view', pk=advert.pk)


class AdvertDeleteView(UserPassesTestMixin, DeleteView):
    model = Advert
    success_url = reverse_lazy('webapp:index')

    def delete_view(request, pk):
        advert = get_object_or_404(Advert, pk=pk)
        if request.method == 'POST':
            advert.is_delete = True
            advert.save()
            return redirect('webapp:index')

