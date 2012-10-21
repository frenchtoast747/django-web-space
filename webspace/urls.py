from django.conf.urls import patterns, include, url

urlpatterns = patterns('webspace.views',
    url(r'^$', 'index', name='index'),
    url(r'^myfiles/$', 'displayfilesview', name='displayfilesview'),
    url(r'^(?P<user_id>\d+)/(?P<slug>[-_.\w]+)$', 'fileview', name='fileview'),
)
