from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signin/$', views.register_view, name='register_url'),
    url(r'^$', views.home_view, name='home_url'),
    url(r'^login/$', views.login_view, name='login_url'),
    url(r'^logout/$', views.logout_view, name='logout_url'),
    #  url(r'^chat/', views.get_chat),
]
