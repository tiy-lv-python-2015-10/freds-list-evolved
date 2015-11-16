from django.db.models import Count
from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions, filters
from rest_framework.throttling import AnonRateThrottle
from api.permissions import IsOwnerOrReadOnly

from api.serializers import StateSerializer, PostSerializer
# CitySerializer, CategorySerializer, SubCategorySerializer, PostSerializer, ImagesSerializer

from fredslist.models import State, City, Category, SubCategory, Post, Images




class SmallPagination(PageNumberPagination):
    page_size = 50


class APIListCreatePost(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'states'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('posting_title', 'specific_location', 'posting_body')

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    throttle_scope = 'states'


class APIListTopPosts(generics.ListAPIView):
    queryset = Post.objects.all().annotate(fav_count=Count('favorite')).order_by('-fav_count')
    serializer_class = PostSerializer
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'states'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('posting_title', 'specific_location', 'posting_body')

    def perform_create(self, serializer):
        serializer.save()

