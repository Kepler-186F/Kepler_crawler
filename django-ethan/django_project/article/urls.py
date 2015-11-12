from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
    # Examples:
	url(r'^all/$','article.views.articles'),
	url(r'^hello/$','article.views.hello'),
	url(r'^hello_template/$','article.views.hello_template'),
	url(r'^get/(?P<article_id>\d+)/$','article.views.article'),
	url(r'^googlechart/$','article.views.google'),	
	url(r'^googlechart2/$','article.views.crawler'),###currently using
	url(r'^search/$','article.views.crawler_search'),
	
	url(r'^dashboard/$','article.views.dashboard'),
)


