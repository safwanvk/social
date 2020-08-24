from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('new/', views.CreateGroup.as_view(), name='create')
]