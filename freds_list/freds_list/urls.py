"""freds_list URL Configuration

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
from django.contrib import admin
from freds_list import settings
from fredslist.views import  PostDetail, PostList, CreatePost, EditPost, DeletePost, CategoryList, StateList
from users.views import CreateUser
from django.conf.urls.static import static

urlpatterns = [

    ####################  REGISTRATION AND HOMEPAGE ##########
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', StateList.as_view(), name="home"),
    url(r'^register/', CreateUser.as_view(), name='register'),



    ####################  CATEGORIES and SUBCATEGORIES ##########
    url(r'^categories/', CategoryList.as_view(), name="category_list"),



    ##################    GENERAL POST URLS ##############
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(),name='post_detail'),
    url(r'^posts/', PostList.as_view(), name="posts"),
    url(r'^create_post/$', CreatePost.as_view(), name='post_create'),
    url(r'^update_post/(?P<pk>\d+)', EditPost.as_view(), name='post_edit'),
    url(r'^delete_post/(?P<pk>\d+)', DeletePost.as_view(), name='post_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
