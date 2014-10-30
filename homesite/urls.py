from django.conf.urls import patterns, include, url
from django.contrib import admin
from homesite.views import current_datetime,current_datetime2,hours_ahead
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^time/$',current_datetime),
    url(r'^time2/$',current_datetime2),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
)
