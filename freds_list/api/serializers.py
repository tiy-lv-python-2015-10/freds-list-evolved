from django.contrib.auth.models import User
from rest_framework import serializers
from fredslist.models import State, City, Category, SubCategory, Post, Images, Favorite


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('state',)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('state',)


class CatgorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('state',)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('state',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'favorited_posts', 'phone_number', 'contact_name', 'posting_title', 'price', 'specific_location',
            'postal_code', 'posting_body',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('state',)


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('state',)
