from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    #url(r'^$', views.view_home, name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^posts/$', views.view_posts, name='post-list'),
    url(r'^posts/(\d+)/$', views.view_post, name='post-detail'),
#    url(r'^posts/create/$', views.view_post_create, name='post-create'),
    url(r'^admin/', include(admin.site.urls)),
]
