from django.conf.urls import url

from social.posts import views

app_name = 'posts'

urlpatterns = [
    url('', views.PostList.as_view(), name='posts')
]