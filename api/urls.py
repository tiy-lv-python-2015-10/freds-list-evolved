from django.conf.urls import url
from api.views import ListCreatePosts, DetailUpdatePost

urlpatterns = [
    url(r'posts/(?P<pk>\d+)', DetailUpdatePost.as_view(),
        name='api_post_detail_update'),
    url(r'posts/top/(?P<top50>\w+)/', ListCreatePosts.as_view(),
        name='api_top_50'),
    url(r'posts/$', ListCreatePosts.as_view(), name='api_post_list_create'),

]