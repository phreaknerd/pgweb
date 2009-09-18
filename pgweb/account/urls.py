from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^$', 'account.views.home'),
    
    # News & Events
    (r'^news/(.*)/$', 'news.views.form'),
    (r'^events/(.*)/$', 'events.views.form'),

    # Log in
    (r'^login/$', 'account.views.login'),

    # Log out
    (r'^logout/$', 'account.views.logout'),
)