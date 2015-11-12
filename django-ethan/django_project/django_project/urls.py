from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import HelloTemplate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello$','article.views.hello'),
    (r'^articles/',include('article.urls')),
    (r'^$','article.views.dashboard'),
)
