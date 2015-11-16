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
from django.contrib.auth.decorators import login_required
from api.views import APIDetailUpdatePost, APIListCreatePost, APIListTopPosts
from freds_list import settings
import fredslist
from fredslist.views import  PostDetail, PostList, CreatePost, EditPost, DeletePost,  StateList, CityDetail, \
    MyPostList, TopPostList
from users.views import CreateUser
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken import views





urlpatterns = [

    ####################  REGISTRATION/ ADMIN/ LOGIN ##########
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', StateList.as_view(), name="home"),
    url(r'^register/', CreateUser.as_view(), name='register'),


    ####################  SHARED (anyone can access) ##########
    url(r'^posts/search$', 'fredslist.views.search',name='post_search'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(),name='post_detail'),
    url(r'^top_posts/', TopPostList.as_view(), name="top_post_list"),
    url(r'^posts/', PostList.as_view(), name="post_list"),
    url(r'^city/(?P<pk>\d+)/$', CityDetail.as_view(),name='city_detail'),


    ####################  FREDSLIST ADMIN ##########
    url(r'^home/', MyPostList.as_view(), name='home_page'),
    url(r'^create_post/$', login_required(CreatePost.as_view()), name='post_create'),
    url(r'^update_post/(?P<pk>\d+)', login_required(EditPost.as_view()), name='post_edit'),
    url(r'^delete_post/(?P<pk>\d+)', login_required(DeletePost.as_view()), name='post_delete'),


    ####################  API ##########
    # url(r'^api/(?P<pk>\d+)$', APIDetailUpdateState.as_view(), name='api_state_detail_update'),
    # url(r'^api/$', APIListCreateState.as_view(), name='api_state_list_create'),
    url(r'^api/(?P<pk>\d+)$', APIDetailUpdatePost.as_view(), name='api_post_detail_update'),
    url(r'^api/$', APIListCreatePost.as_view(), name='api_post_list_create'),
    url(r'^api/top_posts/$', APIListTopPosts.as_view(), name='api_top_post_list'),
    # url(r'^api-token-auth/', views.obtain_auth_token),

    url(r'^favorite/(?P<post_id>\d+)/', 'fredslist.views.create_favorite', name='create_favorite'),
    # url(r'^(?P<city_name>[A-Za-z0-9_-]+)$', CategoryList.as_view(), name="category_list"),
    # url(r'^(?P<city_name>[A-Za-z0-9_-]+)$', CategoryList.as_view(), name="category_list"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
