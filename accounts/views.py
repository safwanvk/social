from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import UserCreateForm


class IndexView(TemplateView):
    template_name = 'index.html'


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:signin')
    template_name = 'accounts/signup.html'


class TestView(TemplateView):
    template_name = 'test.html'


class ThanksView(TemplateView):
    template_name = 'thanks.html'
