from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from peteslist.views import LocationList, LocationListHome, ForSalePost, \
    PostDetail, ListPosts

urlpatterns = [
    url(r'^create/$', login_required(ForSalePost.as_view()), name='post'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^$', ListPosts.as_view(), name="list_posts"),
    url(r'^cat/(?P<category>.+)/$', ListPosts.as_view(),
        name='category_posts'),
    url(r'^favorite/(?P<post_id>\d+)/', 'peteslist.views.add_favorite',
        name="add_favorite"),
    url(r'^deletefav/(?P<post_id>\d+)/', 'peteslist.views.delete_favorite',
        name="delete_favorite"),
]
