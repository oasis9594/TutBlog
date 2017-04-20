from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^user/$', views.user, name='user'),
    url(r'^myblogs/$', views.myblogs, name='myblogs'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
    	views.activate, name='activate'), 
]