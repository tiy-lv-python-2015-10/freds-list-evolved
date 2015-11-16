"""fredslist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from freds_list_evolved import settings
from peteslist.views import LocationList, LocationListHome, UserAccount
from users.views import Register


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locations/$', LocationList.as_view(), name='list_locations'),
    url(r'^locations/(?P<city>.+)/$', 'peteslist.views.loc', name='temp_only'),
    url(r'^loc/$', LocationListHome.as_view(), name='locs_list'),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^logout/', 'django.contrib.auth.views.logout',
        {'next_page': '/locations/'}, name='logout'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^posts/', include('peteslist.urls')),
    url(r'^image/', 'peteslist.views.add_image', name='add_image'),
    url(r'^api/', include('api.urls')),
    url(r'^account/$', UserAccount.as_view(), name='account'),
    url(r'^account/delete/(?P<keyword_id>\d+)/$',
        'peteslist.views.delete_keyword', name='delete_keyword'),
    url(r'^regenerate/', 'peteslist.views.regenerate_token',
        name='regenerate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
