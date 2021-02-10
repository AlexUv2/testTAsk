from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Alias, Target
from .forms import AliasForm, TargetForm


class BaseView(TemplateView):
    template_name = 'base.html'


class AliasListView(ListView):
    model = Alias
    template_name = 'Alias/alias_list.html'
    context_object_name = 'lists'


class AliasNewView(CreateView):
    model = Alias
    form_class = AliasForm
    template_name = 'Alias/new_alias.html'
    

class TargetNewView(CreateView):
    model = Target
    form_class = TargetForm
    template_name = 'Alias/new_target.html'


class TargetListView(ListView):
    model = Target
    template_name = 'Alias/target_list.html'
    context_object_name = 'targets'


class AliasUpdateView(UpdateView):
    model = Alias
    fields = '__all__'
    template_name = 'Alias/alias_edit.html'


class AliasDeleteView(DeleteView):
    model = Alias
    template_name = 'Alias/alias_delete.html'
    success_url = reverse_lazy('list')


class TargetUpdateView(UpdateView):
    model = Target
    fields = '__all__'
    template_name = 'Alias/target_edit.html'


class TargetDeleteView(DeleteView):
    model = Target
    template = 'Alias/target_delete.html'
    success_url = reverse_lazy('target')