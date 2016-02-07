from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HelloWorldView
from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boardgames.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', HelloWorldView.as_view(), name='home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^$', views.index, name='index'),	
    url(r'^admin/', include(admin.site.urls)),
)
