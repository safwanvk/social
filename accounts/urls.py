from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import IndexView

app_name = 'accounts'

urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('signin/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='signin'),
   path('signout/', auth_views.LogoutView.as_view(template_name='accounts/login.html'), name='signout'),
   path('signup/', views.SignUp.as_view(), name='signup'),
   path('test/', views.TestView.as_view(), name='test'),
   path('thanks/', views.ThanksView.as_view(), name='thanks')

]