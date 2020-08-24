from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView 

from . models import Group, GroupMember


# Create your views here.
class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Group
    template_name = 'groups/group_form.html'

class SingleGroup(DetailView):
    model = Group

