from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('spark_chess.core.views',
    url(r'^$', 'home', name='home'),
)

