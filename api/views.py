from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from api.permissions import IsOwnerOrReadOnly
from api.serializers import UserSerializer, PostSerializer
from peteslist.models import Post


class SmallPagination(PageNumberPagination):
    page_size = 5


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCreatePosts(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )



    def perform_create(self, serializer):
        human = self.request.user
        serializer.save(user=human)

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username:
            qs = qs.filter(user__username=username)
        top50 = self.kwargs.get('top50', None)
        if top50 == 'top50':
            qs = qs.annotate(fav_count=Count('favorite')).\
                order_by('-fav_count')[:50]
        return qs


class DetailUpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
