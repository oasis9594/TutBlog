from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^create/$', views.create_blog, name='create_blog'),
    url(r'^$', views.blog_index, name='blog_index'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^recent/$', views.recent, name='recent'),
    url(r'^category/data-structures/$', views.data_structures, name='data_structures'),
    url(r'^category/algorithms/$', views.algorithms, name='algorithms'),
    url(r'^(?P<pk>[0-9]+)/$', views.BlogDetail.as_view(), name='blog_detail'),
]