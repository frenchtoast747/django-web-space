from django.conf.urls import patterns, include, url

urlpatterns = patterns('webspace.views',
    url(r'^$', 'index', name='index'),
)
