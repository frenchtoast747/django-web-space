from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login' ),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout' ),
    url(r'^accounts/register/$', 'webspace.views.register', name='register'),
)
urlpatterns += patterns('webspace.views',
    url(r'^$', 'index', name='index'),
    url(r'^myfiles/$', 'displayfilesview', name='displayfilesview'),
    url(r'^delete/(?P<user_id>\d+)/(?P<slug>[-_.\w]+)$', 'deletefile', name='deletefile'),
    url(r'^(?P<user_id>\d+)/(?P<slug>[-_.\w]+)$', 'fileview', name='fileview'),
)
